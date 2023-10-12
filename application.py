from smi_python_runner.services.arguments_register_service import arguments_register_service
from smi_python_runner.services.runner_register_service import runner_register_service
from smi_python_tbi_parser.constants import SMI_TBI_FILE_ARGUMENT

from smi_python_tbi_runner.tbi_runner import TBIRunner


def register():
    arguments_register_service.register(SMI_TBI_FILE_ARGUMENT)
    runner_register_service.register(TBIRunner())
