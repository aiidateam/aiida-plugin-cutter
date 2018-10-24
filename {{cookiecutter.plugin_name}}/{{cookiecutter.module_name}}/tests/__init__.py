""" tests for the plugin

Use the aiida.utils.fixtures.PluginTestCase class for convenient
testing that does not pollute your profiles/databases.
"""

# Helper functions for tests
from __future__ import absolute_import
import os
import tempfile
import {{cookiecutter.module_name}}.utils as utils

TEST_DIR = os.path.dirname(os.path.realpath(__file__))
TEST_COMPUTER = 'localhost-test'

executables = {
    '{{cookiecutter.entry_point_prefix}}': 'diff',
}

def get_backend_str():
    """ Return database backend string.

    Reads from 'TEST_AIIDA_BACKEND' environment variable.
    Defaults to django backend.
    """
    from aiida.backends.profile import BACKEND_DJANGO, BACKEND_SQLA
    if os.environ.get('TEST_AIIDA_BACKEND') == BACKEND_SQLA:
        return BACKEND_SQLA
    return BACKEND_DJANGO

def get_backend():
    """ Return database backend object.

    Uses get_backend().
    """
    from aiida.orm.backend import construct_backend
    return construct_backend(backend_type=get_backend_str())

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


def get_computer(name=TEST_COMPUTER):
    """Get local computer.

    Sets up local computer with 'name' or reads it from database,
    if it exists.
    
    :param name: Name of local computer

    :return: The computer node 
    :rtype: :py:class:`aiida.orm.Computer` 
    """
    from aiida.orm import Computer
    from aiida.common.exceptions import NotExistent

    if utils.AIIDA_VERSION < utils.StrictVersion('1.0a0'):
        try:
            computer = Computer.get(name)
        except NotExistent:
            # pylint: disable=abstract-class-instantiated,no-value-for-parameter, unexpected-keyword-arg
            computer = Computer(
                name=name,
                description='localhost computer set up by aiida_diff tests',
                hostname=TEST_COMPUTER,
                workdir=tempfile.mkdtemp(),
                transport_type='local',
                scheduler_type='direct',
                enabled_state=True)
    #TODO: simpify once API improvements are in place
    else:
        backend = get_backend()

        try:
            computer = backend.computers.get(name=name)
        except NotExistent:
            computer = backend.computers.create(
                name=name,
                description='localhost computer set up by aiida_diff tests',
                hostname=TEST_COMPUTER,
                workdir=tempfile.mkdtemp(),
                transport_type='local',
                scheduler_type='direct',
                enabled_state=True)

    computer.store()

    return computer


def get_code(entry_point, computer_name=TEST_COMPUTER):
    """Get local code.

    Sets up code for given entry point on given computer.
    
    :param entry_point: Entry point of calculation plugin
    :param computer_name: Name of (local) computer

    :return: The code node 
    :rtype: :py:class:`aiida.orm.Code` 
    """
    from aiida.orm import Code
    from aiida.common.exceptions import NotExistent

    computer = get_computer(computer_name)

    try:
        executable = executables[entry_point]
    except KeyError:
        raise KeyError(
            "Entry point {} not recognized. Allowed values: {}".format(
                entry_point, list(executables.keys())))

    try:
        code = Code.get_from_string('{}@{}'.format(executable, computer_name))
    except NotExistent:
        path = get_path_to_executable(executable)
        code = Code(
            input_plugin_name=entry_point,
            remote_computer_exec=[computer, path],
        )
        code.label = executable
        code.store()

    return code
