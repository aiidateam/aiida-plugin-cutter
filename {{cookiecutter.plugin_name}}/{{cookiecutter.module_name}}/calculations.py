"""
Calculations provided by {{cookiecutter.module_name}}.

Register calculations via the "aiida.calculations" entry point in setup.json.
"""

from __future__ import absolute_import
from aiida.engine import CalcJob
from aiida.orm import SinglefileData
from aiida.common.datastructures import (CalcInfo, CodeInfo)
from aiida.plugins import DataFactory
import six

DiffParameters = DataFactory('{{cookiecutter.entry_point_prefix}}')


class DiffCalculation(CalcJob):
    """
    AiiDA calculation plugin wrapping the diff executable.
    
    Simple AiiDA plugin wrapper for 'diffing' two files.
    """

    _OUTPUT_FILE_NAME = 'patch.diff'

    # {{cookiecutter.entry_point_prefix}}.product entry point defined in setup.json
    _DEFAULT_PARSER = '{{cookiecutter.entry_point_prefix}}'

    @classmethod
    def define(cls, spec):
        """
        Define inputs of calculation.
        
        """
        super(DiffCalculation, cls).define(spec)

        spec.input(
            'metadata.options.parser_name',
            valid_type=six.string_types,
            default=cls._DEFAULT_PARSER)
        spec.input('metadata.options.output_filename', valid_type=six.string_types, default=cls._OUTPUT_FILE_NAME)

        spec.input(
            'metadata.options.parser_name',
            valid_type=six.string_types,
            default=cls._DEFAULT_PARSER)

        spec.input(
            'parameters',
            valid_type=DiffParameters,
            help='Command line parameters for diff')
        spec.input(
            'file1',
            valid_type=SinglefileData,
            help='First file to be compared.')
        spec.input(
            'file2',
            valid_type=SinglefileData,
            help='Second file to be compared.')

        spec.output(
            '{{cookiecutter.entry_point_prefix}}',
            valid_type=SinglefileData,
            help='diff between file1 and file2.')

    def prepare_for_submission(self, folder):
        """
        Create input files.

        :param folder: an `aiida.common.folders.Folder` where the plugin should temporarily place all files needed by the calculation.
        :return: `aiida.common.datastructures.CalcInfo` instance

        """
        # Prepare CalcInfo to be returned to aiida
        calcinfo = CalcInfo()
        calcinfo.uuid = self.uuid

        calcinfo.local_copy_list = [
            (self.inputs.file1.uuid, self.inputs.file1.filename, self.inputs.file1.filename),
            (self.inputs.file2.uuid, self.inputs.file2.filename, self.inputs.file2.filename),
        ]
        calcinfo.remote_copy_list = []
        calcinfo.retrieve_list = [ self._OUTPUT_FILE_NAME ]

        codeinfo = CodeInfo()
        codeinfo.cmdline_params = self.inputs.parameters.cmdline_params(
            file1_name=self.inputs.file1.filename, file2_name=self.inputs.file2.filename)
        codeinfo.code_uuid = self.inputs.code.uuid
        codeinfo.withmpi = False
        codeinfo.stdout_name = self._OUTPUT_FILE_NAME

        calcinfo.codes_info = [codeinfo]

        return calcinfo
