""" Tests for calculations

"""
from __future__ import print_function
from __future__ import absolute_import

from aiida.manage.fixtures import PluginTestCase


class TestDataCli(PluginTestCase):
    def setUp(self):
        from click.testing import CliRunner
        from aiida.plugins import DataFactory

        DiffParameters = DataFactory('{{cookiecutter.entry_point_prefix}}')
        self.parameters = DiffParameters({'ignore-case': True})
        self.parameters.store()
        self.runner = CliRunner()

    def test_data_diff_list(self):
        """Test whether 'verdi data {{cookiecutter.entry_point_prefix}} list' can be reached"""
        from {{cookiecutter.module_name}}.cli import list_

        self.runner.invoke(list_, catch_exceptions=False)

    def test_data_diff_export(self):
        """Test whether 'verdi data {{cookiecutter.entry_point_prefix}} export' can be reached"""
        from {{cookiecutter.module_name}}.cli import export

        self.runner.invoke(export, [str(self.parameters.pk)], catch_exceptions=False)
