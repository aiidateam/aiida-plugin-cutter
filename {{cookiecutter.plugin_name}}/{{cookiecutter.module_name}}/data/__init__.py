# -*- coding: utf-8 -*-
"""
Data types provided by plugin

Register data types via the "aiida.data" entry point in setup.json.
"""

# You can directly use or subclass aiida.orm.data.Data
# or any other data type listed under 'verdi data'
from __future__ import absolute_import
from aiida.orm import Dict
from voluptuous import Schema, Optional

# A subset of diff's command line options
cmdline_options = {
    Optional('ignore-case'): bool,
    Optional('ignore-file-name-case'): bool,
    Optional('ignore-tab-expansion'): bool,
    Optional('ignore-space-change'): bool,
    Optional('ignore-all-space'): bool,
}


class DiffParameters(Dict):
    """
    Command line options for diff.
    """

    schema = Schema(cmdline_options)

    # pylint: disable=redefined-builtin
    def __init__(self, dict=None, **kwargs):
        """
        Constructor for the data class

        Usage: ``DiffParameters(dict{'ignore-case': True})``

        """
        dict = self.validate(dict)
        super(DiffParameters, self).__init__(dict=dict, **kwargs)

    def validate(self, parameters_dict):
        """Validate command line options."""
        return DiffParameters.schema(parameters_dict)

    def cmdline_params(self, file1_name, file2_name):
        """Synthesize command line parameters.

        e.g. [ '--ignore-case', 'filename1', 'filename2']

        :param file_name1: Name of first file
        :param file_name2: Name of second file

        """
        parameters = []

        pm_dict = self.get_dict()
        for k in pm_dict.keys():
            parameters += ['--' + k]

        parameters += [file1_name, file2_name]

        return [str(p) for p in parameters]
