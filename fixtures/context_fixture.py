import pytest


@pytest.fixture
def pw_context(pw_browser):

    pw_context = pw_browser.new_context()

    yield pw_context

    pw_context.close()