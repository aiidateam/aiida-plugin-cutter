import json

from aiida.orm.calculation.job import JobCalculation
from aiida.common.utils import classproperty
from aiida.common.exceptions import (InputValidationError, ValidationError)
from aiida.common.datastructures import (CalcInfo, CodeInfo)
from aiida.orm import DataFactory

MultiplyParameters = DataFactory('{{cookiecutter.entry_point_prefix}}.factors')


class MultiplyCalculation(JobCalculation):
    """
    AiiDA calculation plugin for simple "multiplication"
    
    Simple AiiDA plugin for wrapping a code that adds two numbers.
    """

    def _init_internal_params(self):
        """
        Init internal parameters at class load time
        """
        # reuse base class function
        super(MultiplyCalculation, self)._init_internal_params()

        self._INPUT_FILE_NAME = 'in.json'
        self._OUTPUT_FILE_NAME = 'out.json'
        # {{cookiecutter.entry_point_prefix}}.product entry point defined in setup.json
        self._default_parser = '{{cookiecutter.entry_point_prefix}}.product'

    @classproperty
    def _use_methods(cls):
        """
        Add use_* methods for calculations.
        
        Code below enables the usage
        my_calculation.use_parameters(my_parameters)
        """
        use_dict = JobCalculation._use_methods
        use_dict.update({
            "parameters": {
                'valid_types': MultiplyParameters,
                'additional_parameter': None,
                'linkname': 'parameters',
                'docstring':
                ("Use a node that specifies the input parameters ")
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
        try:
            parameters = inputdict.pop(self.get_linkname('parameters'))
        except KeyError:
            raise InputValidationError("No parameters specified for this "
                                       "calculation")
        if not isinstance(parameters, MultiplyParameters):
            raise InputValidationError("parameters not of type "
                                       "MultiplyParameters")
        try:
            code = inputdict.pop(self.get_linkname('code'))
        except KeyError:
            raise InputValidationError("No code specified for this "
                                       "calculation")
        if inputdict:
            raise ValidationError("Unknown inputs besides MultiplyParameters")

        # In this example, the input file is simply a json dict.
        # Adapt for your particular code!
        input_dict = parameters.get_dict()

        # Write input to file
        input_filename = tempfolder.get_abs_path(self._INPUT_FILE_NAME)
        with open(input_filename, 'w') as infile:
            json.dump(input_dict, infile)

        # Prepare CalcInfo to be returned to aiida
        calcinfo = CalcInfo()
        calcinfo.uuid = self.uuid
        calcinfo.local_copy_list = []
        calcinfo.remote_copy_list = []
        calcinfo.retrieve_list = [self._OUTPUT_FILE_NAME]

        codeinfo = CodeInfo()
        # will call ./code.py in.json out.json
        codeinfo.cmdline_params = [
            self._INPUT_FILE_NAME, self._OUTPUT_FILE_NAME
        ]
        codeinfo.code_uuid = code.uuid
        calcinfo.codes_info = [codeinfo]

        return calcinfo
