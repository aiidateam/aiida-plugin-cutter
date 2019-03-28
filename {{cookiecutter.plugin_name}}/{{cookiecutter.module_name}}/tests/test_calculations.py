""" Tests for calculations

"""
from __future__ import print_function
from __future__ import absolute_import

import os
import {{cookiecutter.module_name}}.tests as tests
import pytest



# pylint: disable=unused-argument,too-many-locals
@pytest.mark.process_execution
def test_process(clear_database, new_workdir):
    """Test running a calculation
    note this does not test that the expected outputs are created of output parsing"""
    from aiida.plugins import DataFactory, CalculationFactory
    from aiida.engine import run_get_node

    # get code
    computer = tests.get_computer(workdir=new_workdir)
    code = tests.get_code(entry_point='{{cookiecutter.entry_point_prefix}}', computer=computer)

    # Prepare input parameters
    DiffParameters = DataFactory('{{cookiecutter.entry_point_prefix}}')
    parameters = DiffParameters({'ignore-case': True})

    from aiida.orm import SinglefileData
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

    _result, node = run_get_node(CalculationFactory('{{cookiecutter.entry_point_prefix}}'), **inputs)

    computed_diff = node.outputs.{{cookiecutter.entry_point_prefix}}.get_content()
    assert 'content1' in computed_diff
    assert 'content2' in computed_diff


