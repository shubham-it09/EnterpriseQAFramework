import pytest
from config.config_manager import config

@pytest.fixture
def pw_page(pw_context):

    pw_page = pw_context.new_page()
    pw_page.set_default_timeout(config.timeout)
    pw_page.set_default_navigation_timeout(config.timeout)

    yield pw_page

    pw_page.close()