"""
For pytest 
initialise a text database and profile
"""
from __future__ import absolute_import
import tempfile
import shutil
import pytest

from aiida.manage.fixtures import fixture_manager


@pytest.fixture(scope='session', autouse=True)
def aiida_profile():
    """Set up a test profile for the duration of the tests"""
    with fixture_manager() as fixture_mgr:
        yield fixture_mgr


@pytest.fixture(scope='function', autouse=True)
def clear_database(aiida_profile):
    """Clear the database after each test"""
    yield
    aiida_profile.reset_db()


@pytest.fixture(scope='function')
def new_workdir():
    """Get a temporary folder to use as the computer's work directory."""
    dirpath = tempfile.mkdtemp()
    yield dirpath
    shutil.rmtree(dirpath)


@pytest.fixture(scope='function')
def aiida_localhost_computer(new_workdir):
    """Get an AiiDA computer for localhost.

    :return: The computer node
    :rtype: :py:class:`aiida.orm.Computer`
    """
    from {{cookiecutter.module_name}}.helpers import get_computer

    computer = get_computer(workdir=new_workdir)

    return computer


@pytest.fixture(scope='function')
def aiida_code(aiida_localhost_computer):
    """Get an AiiDA code.

    :return: The code node
    :rtype: :py:class:`aiida.orm.Code`
    """
    from {{cookiecutter.module_name}}.helpers import get_code

    code = get_code(entry_point='{{cookiecutter.entry_point_prefix}}', computer=aiida_localhost_computer)

    return code
