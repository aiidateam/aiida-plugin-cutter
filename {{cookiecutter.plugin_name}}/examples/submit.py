# -*- coding: utf-8 -*-
"""Submit a test calculation on localhost.

Usage: verdi run submit.py
"""
from __future__ import absolute_import
from __future__ import print_function
import os
import {{cookiecutter.module_name}}.tests as tests
from aiida.plugins import DataFactory, CalculationFactory
from aiida.engine import run

# get code
computer = tests.get_computer()
code = tests.get_code(entry_point='{{cookiecutter.entry_point_prefix}}', computer=computer)

# Prepare input parameters
DiffParameters = DataFactory('{{cookiecutter.entry_point_prefix}}')
parameters = DiffParameters({'ignore-case': True})

SinglefileData = DataFactory('singlefile')
file1 = SinglefileData(
    file=os.path.join(tests.TEST_DIR, "input_files", 'file1.txt'))
file2 = SinglefileData(
    file=os.path.join(tests.TEST_DIR, "input_files", 'file2.txt'))

# set up calculation
options = {
    "resources": {
        "num_machines": 1,
        "num_mpiprocs_per_machine": 1,
    },
    "max_wallclock_seconds": 30,
}

inputs = {
    'code': code,
    'parameters': parameters,
    'file1': file1,
    'file2': file2,
    'metadata': {
        'options': options,
        'label': "{{cookiecutter.module_name}} test",
        'description': "Test job submission with the {{cookiecutter.module_name}} plugin",
    },
}

# Note: in order to submit your calculation to the aiida daemon, do:
# from aiida.engine import submit
# future = submit(CalculationFactory('{{cookiecutter.entry_point_prefix}}'), **inputs)
result = run(CalculationFactory('{{cookiecutter.entry_point_prefix}}'), **inputs)

computed_diff = result['{{cookiecutter.entry_point_prefix}}'].get_content()
print("Computed diff between files: \n{}".format(computed_diff))
