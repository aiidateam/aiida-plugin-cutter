# -*- coding: utf-8 -*-
"""
Parsers provided by {{cookiecutter.module_name}}.

Register parsers via the "aiida.parsers" entry point in setup.json.
"""
from __future__ import absolute_import

from six.moves import zip

from aiida.engine import ExitCode
from aiida.parsers.parser import Parser
from aiida.common import exceptions
from aiida.plugins import CalculationFactory

DiffCalculation = CalculationFactory('{{cookiecutter.entry_point_prefix}}')

class DiffParser(Parser):
    """
    Parser class for parsing output of calculation.
    """

    def __init__(self, node):
        """
        Initialize Parser instance
        """
        super(DiffParser, self).__init__(node)
        if not issubclass(node.process_class, DiffCalculation):
            raise exceptions.ParsingError("Can only parse DiffCalculation")

    def parse(self, **kwargs):
        """
        Parse outputs, store results in database.

        :returns: an exit code, if parsing fails (or nothing if parsing succeeds)
        """
        from aiida.orm import SinglefileData

        # Check that the retrieved folder is there
        try:
            output_folder = self.retrieved
        except exceptions.NotExistent:
            return self.exit_codes.ERROR_NO_RETRIEVED_FOLDER

        # Check the folder content is as expected
        list_of_files = output_folder.list_object_names()
        output_files = [self.node.get_option('output_filename')]
        output_links = ['{{cookiecutter.entry_point_prefix}}']
        # Note: set(A) <= set(B) checks whether A is a subset
        if set(output_files) <= set(list_of_files):
            pass
        else:
            self.logger.error("Not all expected output files {} were found".
                              format(output_files))

        # Use something like this to loop over multiple output files
        for fname, link in zip(output_files, output_links):

            with output_folder.open(fname) as handle:
                node = SinglefileData(file=handle)
            self.out(link, node)

        return ExitCode(0)
