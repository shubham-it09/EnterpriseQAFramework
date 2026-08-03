pytest_plugins = [
    "fixtures.browser_fixture",
    "fixtures.context_fixture",
    "fixtures.page_fixture",
    "fixtures.logger_fixture",
    "fixtures.login_business_fixture",
    "fixtures.admin_business_fixture",
    "fixtures.screenshot_fixture",
    "api.fixtures.api_client_fixture",
    "fixtures.config_fixture",
    "api.fixtures.booking_business_fixture",
    "api.fixtures.auth_business_fixture",
   

]

import pytest

from core.test_failure_handler import TestFailureHandler

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield

    report = outcome.get_result()

    TestFailureHandler.handle(
        item=item,
        call=call,
        report=report
    )