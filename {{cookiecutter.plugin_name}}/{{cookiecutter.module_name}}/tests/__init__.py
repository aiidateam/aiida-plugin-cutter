""" tests for the plugin

Use the aiida.utils.fixtures.PluginTestCase class for convenient
testing that does not pollute your profiles/databases.
"""

# Helper functions for tests
import os
import stat
import subprocess
import sys

TEST_DIR = os.path.dirname(os.path.realpath(__file__))
TEST_COMPUTER = 'localhost-test'

executables = {
    '{{cookiecutter.entry_point_prefix}}': 'diff',
}


def get_backend():
    """ Return database backend.

    Reads from 'TEST_AIIDA_BACKEND' environment variable.
    Defaults to django backend.
    """
    from aiida.backends.profile import BACKEND_DJANGO, BACKEND_SQLA
    if os.environ.get('TEST_AIIDA_BACKEND') == BACKEND_SQLA:
        return BACKEND_SQLA
    return BACKEND_DJANGO


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


def get_computer(name=TEST_COMPUTER, workdir=None):
    """Get local computer.

    Sets up local computer with 'name' or reads it from database,
    if it exists.
    
    :param name: Name of local computer
    :param workdir: path to work directory (required if creating a new computer)

    :return: The computer node 
    :rtype: :py:class:`aiida.orm.Computer` 
    """
    from aiida.orm import Computer
    from aiida.common.exceptions import NotExistent

    try:
        computer = Computer.get(name)
    except NotExistent:

        if workdir is None:
            raise ValueError("to create a new computer, a work directory must be supplied")

        computer = Computer(
            name=name,
            description='localhost computer set up by aiida_crystal17 tests',
            hostname=name,
            workdir=workdir,
            transport_type='local',
            scheduler_type='direct',
            enabled_state=True)
        computer.store()

        # TODO configure computer for user, see aiida_core.aiida.cmdline.commands.computer.Computer.computer_configure

    return computer


def get_code(entry_point, computer):
    """Get local code.

    Sets up code for given entry point on given computer.
    
    :param entry_point: Entry point of calculation plugin
    :param computer_name: Name of (local) computer

    :return: The code node 
    :rtype: :py:class:`aiida.orm.Code` 
    """
    from aiida.orm import Code
    from aiida.common.exceptions import NotExistent

    try:
        executable = executables[entry_point]
    except KeyError:
        raise KeyError("Entry point {} not recognized. Allowed values: {}"
                       .format(entry_point, executables.keys()))

    try:
        code = Code.get_from_string('{}@{}'.format(executable, computer.get_name()))
    except NotExistent:
        path = get_path_to_executable(executable)
        code = Code(
            input_plugin_name=entry_point,
            remote_computer_exec=[computer, path],
        )
        code.label = executable
        code.store()

    return code
