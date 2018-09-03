from __future__ import absolute_import
import sys
import unittest
from {{cookiecutter.module_name}}.tests import get_backend
from aiida.utils.fixtures import TestRunner

tests = unittest.defaultTestLoader.discover('.')
result = TestRunner().run(tests, backend=get_backend())

exit_code = int(not result.wasSuccessful())
sys.exit(exit_code)
