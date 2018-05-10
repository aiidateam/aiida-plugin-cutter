#!/usr/bin/env runaiida
# -*- coding: utf-8 -*-
import sys
import os
import click


@click.command('cli')
@click.argument('codename')
@click.argument('computer_name')
@click.option('--submit', is_flag=True, help='Actually submit calculation')
def main(codename, computer_name, submit):
    """Command line interface for testing and submitting calculations.

    Usage: ./cli.py CODENAME COMPUTER_NAME
    
    CODENAME       from "verdi code setup"

    COMPUTER_NAME  from "verdi computer setup"

    This script extends submit.py, adding flexibility in the selected code/computer.
    """
    from aiida.common.exceptions import NotExistent

    code = Code.get_from_string(codename)
    computer = Computer.get(computer_name)

    # Prepare input parameters
    MultiplyParameters = DataFactory('{{cookiecutter.entry_point_prefix}}.factors')
    parameters = MultiplyParameters(x1=2, x2=3)

    # set up calculation
    calc = code.new_calc()
    calc.label = "{{cookiecutter.module_name}} computes 2*3"
    calc.description = "Test job submission with the {{cookiecutter.module_name}} plugin"
    calc.set_max_wallclock_seconds(30 * 60)  # 30 min
    # This line is only needed for local codes, otherwise the computer is
    # automatically set from the code
    calc.set_computer(computer)
    calc.set_withmpi(False)
    calc.set_resources({"num_machines": 1})
    calc.use_parameters(parameters)

    if submit:
        calc.store_all()
        calc.submit()
        print("submitted calculation; calc=Calculation(uuid='{}') # ID={}"\
                .format(calc.uuid,calc.dbnode.pk))
    else:
        subfolder, script_filename = calc.submit_test()
        path = os.path.relpath(subfolder.abspath)
        print("submission test successful")
        print("Find remote folder in {}".format(path))
        print("In order to actually submit, add '--submit'")


if __name__ == '__main__':
    main()
