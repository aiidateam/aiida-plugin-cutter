import unittest
import sys
from aiida.utils.capturing import Capturing
from aiida.utils.fixtures import fixture_manager, _PYTEST_FIXTURE_MANAGER
from {{cookiecutter.module_name}}.tests import get_backend

tests = unittest.defaultTestLoader.discover('.')
runner = unittest.TextTestRunner()

_PYTEST_FIXTURE_MANAGER.backend = get_backend()
with Capturing():
    with fixture_manager() as manager:
        result = runner.run(tests)

exit_code = int(not result.wasSuccessful())
sys.exit(exit_code)
