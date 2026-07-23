import pytest

from config.config_manager import config


@pytest.fixture(scope="session")
def framework_config():
    return config