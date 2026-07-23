import pytest
from config.config_manager import config
import time

@pytest.mark.skip
def test_open_home_page(pw_page):

    pw_page.goto(config.base_url)
    time.sleep(300000)

    # assert "OpenCart" in page.title()