import pytest

from core.browser_manager import BrowserManager


@pytest.fixture(scope="session")
def pw_browser():

    manager = BrowserManager()

    pw_browser = manager.launch_browser()

    yield pw_browser

    manager.close_browser()