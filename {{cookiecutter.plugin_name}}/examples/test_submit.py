# -*- coding: utf-8 -*-
"""Submit a test calculation on localhost.

Usage: verdi run submit.py

Note: This script assumes you have set up computer and code as in README.md.
"""
import os
import {{cookiecutter.module_name}}.tests as tests


def get_code(workdir):
    """get the crystal17.basic code """
    computer = tests.get_computer(workdir=workdir)
    # get code
    code = tests.get_code(
        entry_point='{{cookiecutter.entry_point_prefix}}', computer=computer)

    return code


def test_example(new_database, new_workdir):
    
    code = get_code(new_workdir)

    # Prepare input parameters
    from aiida.orm import DataFactory
    DiffParameters = DataFactory('{{cookiecutter.entry_point_prefix}}')
    parameters = DiffParameters({'ignore-case': True})

    SinglefileData = DataFactory("singlefile")
    file1 = SinglefileData(file=os.path.join(tests.TEST_DIR, "input_files", 'file1.txt'))
    file2 = SinglefileData(file=os.path.join(tests.TEST_DIR, "input_files", 'file2.txt'))

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

    calc.store_all()
    calc.submit()
    print("submitted calculation; calc=Calculation(uuid='{}') # ID={}".format(calc.uuid,calc.dbnode.pk))


if __name__ == "__main__":

    wrkdir = "./aiida_workdir"
    if not os.path.exists(wrkdir):
        os.makedirs("./aiida_workdir")

    test_example(None, "./aiida_workdir")