#!/usr/bin/env runaiida
# -*- coding: utf-8 -*-
import sys
import os
import click


@click.command('cli')
@click.argument('codelabel')
@click.option('--submit', is_flag=True, help='Actually submit calculation')
def main(codelabel, submit):
    """Command line interface for testing and submitting calculations.

    This script extends submit.py, adding flexibility in the selected code/computer.

    Run './cli.py --help' to see options.
    """
    code = Code.get_from_string(codelable)

    # Prepare input parameters
    from aiida.orm import DataFactory
    DiffParameters = DataFactory('{{cookiecutter.entry_point_prefix}}')
    parameters = DiffParameters({'ignore-case': True})

    file1 = SinglefileData(file=os.path.join(tests.TEST_DIR, 'file1.txt'))
    file2 = SinglefileData(file=os.path.join(tests.TEST_DIR, 'file2.txt'))

    # set up calculation
    calc = code.new_calc()
    calc.label = "{{cookiecutter.module_name}} test"
    calc.description = "Test job submission with the {{cookiecutter.module_name}} plugin"
    calc.set_max_wallclock_seconds(30)
    calc.set_withmpi(False)
    calc.set_resources({"num_machines": 1, "num_mpiprocs_per_machine": 1})

    calc.use_parameters(parameters)
    calc.use_file1(file1)
    calc.use_file2(file2)

    if submit:
        calc.store_all()
        calc.submit()
        print("submitted calculation; calc=Calculation(uuid='{}') # ID={}"\
                .format(calc.uuid,calc.dbnode.pk))
    else:
        subfolder, script_filename = calc.submit_test()
        path = os.path.relpath(subfolder.abspath)
        print("Submission test successful.")
        print("Find remote folder in {}".format(path))
        print("In order to actually submit, add '--submit'")


if __name__ == '__main__':
    main()
