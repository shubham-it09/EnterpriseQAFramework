import pytest

from core.logger_manager import LoggerManager


@pytest.fixture
def logger(request):

    return LoggerManager.get_logger(request.node.name)