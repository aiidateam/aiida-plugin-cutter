""" Tests for calculations

"""
import os
import tempfile

from aiida.utils.fixtures import PluginTestCase
from aiida.backends.profile import BACKEND_DJANGO, BACKEND_SQLA


def get_backend():
    if os.environ.get('TEST_AIIDA_BACKEND') == BACKEND_SQLA:
        return BACKEND_SQLA
    return BACKEND_DJANGO


class TestMultiply(PluginTestCase):

    # load the backend to be tested from the environment variable:
    # TEST_AIIDA_BACKEND=django python -m unittest discover
    # TEST_AIIDA_BACKEND=sqlalchemy python -m unittest discover
    BACKEND = get_backend()

    def get_localhost(self):
        """Setup localhost computer"""
        from aiida.orm import Computer
        computer = Computer(
            name='localhost',
            description='my computer',
            hostname='localhost',
            workdir=tempfile.mkdtemp(),
            transport_type='local',
            scheduler_type='direct',
            enabled_state=True)
        return computer

    def get_code(self):
        """Setup code on localhost computer"""
        from aiida.orm import Code

        script_dir = os.path.dirname(__file__)
        executable = os.path.realpath(os.path.join(script_dir, '../code.py'))

        code = Code(
            files=[executable],
            input_plugin_name='{{cookiecutter.entry_point_prefix}}.multiply',
            local_executable='code.py')
        code.label = '{{cookiecutter.entry_point_prefix}}.multiply'
        code.description = 'multiply on this computer'

        return code

    def setUp(self):

        # set up test computer
        self.computer = self.get_localhost().store()
        self.code = self.get_code().store()

    def test_submit(self):
        """Test submitting a calculation"""

        computer = self.computer
        code = self.code
        #from aiida.orm import Code, Computer, DataFactory
        #code = Code.get_from_string('{{cookiecutter.entry_point_prefix}}.multiply')
        #computer = Computer.get('localhost')

        # Prepare input parameters
        from aiida.orm import DataFactory
        MultiplyParameters = DataFactory('{{cookiecutter.entry_point_prefix}}.factors')
        parameters = MultiplyParameters(x1=2, x2=3)

        # set up calculation
        calc = code.new_calc()
        calc.label = "{{cookiecutter.module_name}} computes 2*3"
        calc.description = "Test job submission with the {{cookiecutter.module_name}} plugin"
        calc.set_max_wallclock_seconds(30)
        # This line is only needed for local codes, otherwise the computer is
        # automatically set from the code
        calc.set_computer(computer)
        calc.set_withmpi(False)
        calc.set_resources({"num_machines": 1, "num_mpiprocs_per_machine": 1})
        calc.use_parameters(parameters)

        calc.store_all()
        calc.submit()
        print("submitted calculation; calc=Calculation(uuid='{}') # ID={}"\
                .format(calc.uuid,calc.dbnode.pk))
