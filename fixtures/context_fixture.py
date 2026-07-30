import pytest
from pathlib import Path

SCREENSHOT_DIR = Path("artifacts/screenshots")
SCREENSHOT_DIR.mkdir(parents=True, exist_ok=True)

@pytest.fixture
def pw_context(pw_browser):

    pw_context = pw_browser.new_context()

    yield pw_context

    pw_context.close()