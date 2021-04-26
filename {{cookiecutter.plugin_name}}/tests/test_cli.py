# -*- coding: utf-8 -*-
""" Tests for command line interface.

"""
from click.testing import CliRunner
from aiida.manage.tests.unittest_classes import PluginTestCase
from aiida.plugins import DataFactory

from {{cookiecutter.module_name}}.cli import list_, export

class TestDataCli(PluginTestCase):
    """Test verdi data cli plugin."""

    def setUp(self):
        DiffParameters = DataFactory('{{cookiecutter.entry_point_prefix}}')
        self.parameters = DiffParameters({'ignore-case': True})
        self.parameters.store()
        self.runner = CliRunner()

    def test_data_diff_list(self):
        """Test 'verdi data {{cookiecutter.entry_point_prefix}} list'

        Tests that it can be reached and that it lists the node we have set up.
        """
        result = self.runner.invoke(list_, catch_exceptions=False)
        self.assertIn(str(self.parameters.pk), result.output)

    def test_data_diff_export(self):
        """Test 'verdi data {{cookiecutter.entry_point_prefix}} export'

        Tests that it can be reached and that it shows the contents of the node
        we have set up.
        """
        result = self.runner.invoke(export, [str(self.parameters.pk)],
                                    catch_exceptions=False)
        self.assertIn('ignore-case', result.output)
