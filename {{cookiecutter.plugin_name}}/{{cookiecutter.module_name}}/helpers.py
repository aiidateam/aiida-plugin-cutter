""" Helper functions for automatically setting up computer & code.

Helper functions for setting up 

 1. An AiiDA localhost computer
 2. A "diff" code on localhost
 
Note: Point 2 is made possible by the fact that the ``diff`` executable is
available in the PATH on almost any UNIX system.
"""
from __future__ import absolute_import
from __future__ import print_function
import tempfile

LOCALHOST_NAME = 'localhost-test'

executables = {
    'diff': 'diff',
}


def get_path_to_executable(executable):
    """ Get path to local executable.

    :param executable: Name of executable in the $PATH variable
    :type executable: str

    :return: path to executable
    :rtype: str
    """
    # pylint issue https://github.com/PyCQA/pylint/issues/73
    import distutils.spawn  # pylint: disable=no-name-in-module,import-error
    path = distutils.spawn.find_executable(executable)
    if path is None:
        raise ValueError("{} executable not found in PATH.".format(executable))

    return path


def get_computer(name=LOCALHOST_NAME, workdir=None):
    """Get AiiDA computer.

    Loads computer 'name' from the database, if exists.
    Sets up local computer 'name', if it isn't found in the DB.
    
    :param name: Name of computer to load or set up.
    :param workdir: path to work directory 
        Used only when creating a new computer.

    :return: The computer node 
    :rtype: :py:class:`aiida.orm.Computer` 
    """
    from aiida.orm import Computer
    from aiida.common.exceptions import NotExistent

    try:
        computer = Computer.objects.get(name=name)
    except NotExistent:
        if workdir is None:
            workdir = tempfile.mkdtemp()

        computer = Computer(
            name=name,
            description='localhost computer set up by aiida_diff tests',
            hostname=name,
            workdir=workdir,
            transport_type='local',
            scheduler_type='direct')
        computer.store()
        computer.configure()

    return computer


def get_code(entry_point, computer):
    """Get local code.

    Sets up code for given entry point on given computer.
    
    :param entry_point: Entry point of calculation plugin
    :param computer: (local) AiiDA computer

    :return: The code node 
    :rtype: :py:class:`aiida.orm.Code` 
    """
    from aiida.orm import Code
    from aiida.common.exceptions import NotExistent

    try:
        executable = executables[entry_point]
    except KeyError:
        raise KeyError(
            "Entry point {} not recognized. Allowed values: {}".format(
                entry_point, list(executables.keys())))

    try:
        code = Code.get_from_string('{}@{}'.format(executable,
                                                   computer.get_name()))
    except NotExistent:
        path = get_path_to_executable(executable)
        code = Code(
            input_plugin_name=entry_point,
            remote_computer_exec=[computer, path],
        )
        code.label = executable
        code.store()

    return code
