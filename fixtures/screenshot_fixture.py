import logging
from datetime import datetime

import allure
import pytest

from core.artifact_manager import ArtifactManager


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    # Execute only after actual test execution
    if report.when != "call":
        return

    # Attach artifacts only for failed tests
    if report.passed:
        return

    # ------------------------------------
    # Get xdist worker id
    # ------------------------------------

    worker_id = getattr(
        item.config,
        "workerinput",
        {}
    ).get(
        "workerid",
        "master"
    )

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S_%f"
    )

    # ------------------------------------
    # Screenshot
    # ------------------------------------

    page = item.funcargs.get("pw_page")

    if page is not None:

        screenshot_path = (
            ArtifactManager.get_screenshots_folder()
            / (
                f"{worker_id}_"
                f"{item.name}_"
                f"{timestamp}.png"
            )
        )

        page.screenshot(
            path=str(screenshot_path),
            full_page=True
        )

        allure.attach.file(
            str(screenshot_path),
            name="Failure Screenshot",
            attachment_type=allure.attachment_type.PNG
        )

    # ------------------------------------
    # Log File
    # ------------------------------------

    logger = item.funcargs.get("logger")

    if logger:

        for handler in logger.handlers:

            if isinstance(handler, logging.FileHandler):

                allure.attach.file(
                    handler.baseFilename,
                    name="Execution Log",
                    attachment_type=allure.attachment_type.TEXT
                )

                break