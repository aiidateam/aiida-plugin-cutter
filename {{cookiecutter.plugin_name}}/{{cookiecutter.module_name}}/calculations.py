"""
Calculations provided by {{cookiecutter.module_name}}.

Register calculations via the "aiida.calculations" entry point in setup.json.
"""

from aiida.orm.calculation.job import JobCalculation
from aiida.orm.data.singlefile import SinglefileData
from aiida.common.utils import classproperty
from aiida.common.exceptions import (InputValidationError, ValidationError)
from aiida.common.datastructures import (CalcInfo, CodeInfo)
from aiida.orm import DataFactory

DiffParameters = DataFactory('{{cookiecutter.entry_point_prefix}}')


class DiffCalculation(JobCalculation):
    """
    AiiDA calculation plugin wrapping the diff executable.
    
    Simple AiiDA plugin wrapper for 'diffing' two files.
    """

    _OUTPUT_FILE_NAME = 'patch.diff'

    def _init_internal_params(self):
        """
        Init internal parameters at class load time
        """
        # reuse base class function
        super(DiffCalculation, self)._init_internal_params()

        # {{cookiecutter.entry_point_prefix}}.product entry point defined in setup.json
        self._default_parser = '{{cookiecutter.entry_point_prefix}}'

    @classproperty
    def _use_methods(cls):
        """
        Add use_* methods for calculations.
        
        Code below enables the usage
        my_calculation.use_parameters(my_parameters)
        """
        use_dict = JobCalculation._use_methods
        use_dict.update({
            "diffparameters": {
                'valid_types': DiffParameters,
                'additional_parameter': None,
                'linkname': 'diffparameters',
                'docstring': ("Command line parameters for diff")
            },
            "file1": {
                'valid_types': SinglefileData,
                'additional_parameter': None,
                'linkname': 'file1',
                'docstring': ("First file to be compared.")
            },
            "file2": {
                'valid_types': SinglefileData,
                'additional_parameter': None,
                'linkname': 'file2',
                'docstring': ("Second file to be compared.")
            },
        })
        return use_dict

    def _prepare_for_submission(self, tempfolder, inputdict):
        """
        Create input files.

            :param tempfolder: aiida.common.folders.Folder subclass where
                the plugin should put all its files.
            :param inputdict: dictionary of the input nodes as they would
                be returned by get_inputs_dict
        """
        # Check inputdict
        new_inputdict = inputdict.copy()
        
        try:
            code = new_inputdict.pop(self.get_linkname('code'))
        except KeyError:
            raise InputValidationError("No code specified for this "
                                       "calculation")

        try:
            parameters = new_inputdict.pop(self.get_linkname('diffparameters'))
        except KeyError:
            raise InputValidationError("No parameters specified for this "
                                       "calculation")
        if not isinstance(parameters, DiffParameters):
            raise InputValidationError("parameters not of type "
                                       "DiffParameters: {}".format(parameters))

        try:
            file1 = new_inputdict.pop(self.get_linkname('file1'))
        except KeyError:
            raise InputValidationError("Missing file1")
        if not isinstance(file1, SinglefileData):
            raise InputValidationError("file1 not of type SinglefileData: {}".format(file1))

        try:
            file2 = new_inputdict.pop(self.get_linkname('file2'))
        except KeyError:
            raise InputValidationError("Missing file2")
        if not isinstance(file2, SinglefileData):
            raise InputValidationError("file2 not of type SinglefileData: {}".format(file2))

        if new_inputdict:
            raise ValidationError("Unknown inputs besides DiffParameters")

        # Prepare CodeInfo object for aiida
        codeinfo = CodeInfo()
        codeinfo.code_uuid = code.uuid
        codeinfo.cmdline_params = parameters.cmdline_params(
            file1_name=file1.filename, file2_name=file2.filename)
        codeinfo.stdout_name = self._OUTPUT_FILE_NAME

        # Prepare CalcInfo object for aiida
        calcinfo = CalcInfo()
        calcinfo.uuid = self.uuid
        calcinfo.local_copy_list = []
        calcinfo.remote_copy_list = []
        calcinfo.retrieve_list = [self._OUTPUT_FILE_NAME]
        calcinfo.local_copy_list = [
            [file1.get_file_abs_path(), file1.filename],
            [file2.get_file_abs_path(), file2.filename],
        ]
        calcinfo.codes_info = [codeinfo]

        return calcinfo
