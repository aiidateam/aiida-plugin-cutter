# -*- coding: utf-8 -*-
"""
Command line interface (cli) for {{cookiecutter.module_name}}.

Command line interface for plugin-specific tasks.

Register new command line interfaces either via the "console_scripts" entry
point or plug them into the 'verdi' command by using AiiDA-specific entry
points like "aiida.cmdline.data" in setup.json.
"""
import os
import click
from aiida.cmdline.dbenv_lazyloading import load_dbenv_if_not_loaded
import {{cookiecutter.module_name}}.tests as tests


@click.command('')
@click.argument('codelabel')
@click.option('--submit', is_flag=True, help='Actually submit calculation')
def submit(codelabel, submit):
    """Command line interface for testing and submitting calculations.

    This command is based on examples/submit.py, but adds flexibility in the
    selected code/computer.

    Run ``{{cookiecutter.entry_point_prefix}}-submit --help`` to see options.
    """
    load_dbenv_if_not_loaded(
    )  # Important to load the dbenv in the last moment
    from aiida.orm import Code
    from aiida.orm.data import SinglefileData

    code = Code.get_from_string(codelabel)

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
        subfolder, _script_filename = calc.submit_test()
        path = os.path.relpath(subfolder.abspath)
        print("Submission test successful.")
        print("Find remote folder in {}".format(path))
        print("In order to actually submit, add '--submit'")
