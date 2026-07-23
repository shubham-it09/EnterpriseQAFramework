import pytest

from api.client.api_client import APIClient

from config.config_manager import config



@pytest.fixture(scope="function")
def api_client(framework_config,logger):
    """
    Creates API client.
    """

    client = APIClient(
        base_url=config.api_base_url,
        logger=logger
    )

    yield client

    client.close()