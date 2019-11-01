""" Tests for calculations

"""
from __future__ import print_function
from __future__ import absolute_import

import os
from {{cookiecutter.module_name}} import tests


def test_process({{cookiecutter.entry_point_prefix}}_code):
    """Test running a calculation
    note this does not test that the expected outputs are created of output parsing"""
    from aiida.plugins import DataFactory, CalculationFactory
    from aiida.engine import run

    # Prepare input parameters
    DiffParameters = DataFactory('{{cookiecutter.entry_point_prefix}}')
    parameters = DiffParameters({'ignore-case': True})

    from aiida.orm import SinglefileData
    file1 = SinglefileData(
        file=os.path.join(tests.TEST_DIR, "input_files", 'file1.txt'))
    file2 = SinglefileData(
        file=os.path.join(tests.TEST_DIR, "input_files", 'file2.txt'))

    # set up calculation
    inputs = {
        'code': {{cookiecutter.entry_point_prefix}}_code,
        'parameters': parameters,
        'file1': file1,
        'file2': file2,
        'metadata': {
            'options': {
                'max_wallclock_seconds': 30
            },
        },
    }

    result = run(CalculationFactory('{{cookiecutter.entry_point_prefix}}'), **inputs)
    computed_diff = result['{{cookiecutter.entry_point_prefix}}'].get_content()

    assert 'content1' in computed_diff
    assert 'content2' in computed_diff
