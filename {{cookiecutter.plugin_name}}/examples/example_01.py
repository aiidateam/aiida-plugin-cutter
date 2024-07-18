#!/usr/bin/env python
"""Run a test calculation on localhost.

Usage: ./example_01.py
"""

from os import path

import click
from aiida import cmdline, engine
from aiida.plugins import CalculationFactory, DataFactory
from {{cookiecutter.module_name}} import helpers

INPUT_DIR = path.join(path.dirname(path.realpath(__file__)), 'input_files')


def test_run({{cookiecutter.entry_point_prefix}}_code):
    """Run a calculation on the localhost computer.

    Uses test helpers to create AiiDA Code on the fly.
    """
    if not {{cookiecutter.entry_point_prefix}}_code:
        # get code
        computer = helpers.get_computer()
        {{cookiecutter.entry_point_prefix}}_code = helpers.get_code(
            entry_point='{{cookiecutter.entry_point_prefix}}', computer=computer
        )

    # Prepare input parameters
    diff_parameters = DataFactory('{{cookiecutter.entry_point_prefix}}')
    parameters = diff_parameters({'ignore-case': True})

    singlefile_data = DataFactory('core.singlefile')
    file1 = singlefile_data(file=path.join(INPUT_DIR, 'file1.txt'))
    file2 = singlefile_data(file=path.join(INPUT_DIR, 'file2.txt'))

    # set up calculation
    inputs = {
        'code': {{cookiecutter.entry_point_prefix}}_code,
        'parameters': parameters,
        'file1': file1,
        'file2': file2,
        'metadata': {
            'description': 'Test job submission with the {{cookiecutter.module_name}} plugin',
        },
    }

    # Note: in order to submit your calculation to the aiida daemon, do:
    # from aiida.engine import submit
    # future = submit(CalculationFactory('{{cookiecutter.entry_point_prefix}}'), **inputs)
    result = engine.run(CalculationFactory('{{cookiecutter.entry_point_prefix}}'), **inputs)

    computed_diff = result['{{cookiecutter.entry_point_prefix}}'].get_content()
    print(f'Computed diff between files: \n{computed_diff}')


@click.command()
@cmdline.utils.decorators.with_dbenv()
@cmdline.params.options.CODE()
def cli(code):
    """Run example.

    Example usage: $ ./example_01.py --code diff@localhost

    Alternative (creates diff@localhost-test code): $ ./example_01.py

    Help: $ ./example_01.py --help
    """
    test_run(code)


if __name__ == '__main__':
    cli()  # pylint: disable=no-value-for-parameter
