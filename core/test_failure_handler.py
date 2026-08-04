"""
==============================================================
Test Failure Handler

Author : Shubham Pandey

Description:
------------
Central handler for failed test execution.

Responsibilities
----------------
✓ Detect failed tests
✓ Collect runtime information
✓ Capture screenshot
✓ Build failure context
✓ Invoke AI Root Cause Analyzer
==============================================================
"""

import traceback
from datetime import datetime
from pathlib import Path

from ai.analyzers.root_cause_analyzer import RootCauseAnalyzer
from ai.collectors.failure_collector import FailureCollector
from ai.generators.bug_report_generator import BugReportGenerator


class TestFailureHandler:
    """
    Handles failed test execution.
    """

    SCREENSHOT_DIR = Path("artifacts/screenshots")

    @staticmethod
    def _get_page(item):
        return item.funcargs.get("page")

    @staticmethod
    def _get_browser(item):
        return item.funcargs.get("browser_name", "")

    @classmethod
    def _capture_screenshot(cls, page, test_name: str) -> str:
        """
        Captures screenshot of the failed page.
        """

        if not page:
            return ""

        try:

            cls.SCREENSHOT_DIR.mkdir(
                parents=True,
                exist_ok=True
            )

            screenshot = cls.SCREENSHOT_DIR / f"{test_name}.png"

            page.screenshot(
                path=str(screenshot),
                full_page=True
            )

            return str(screenshot)

        except Exception:
            return ""

    @staticmethod
    def handle(item, call, report):
        """
        Executes AI analysis for failed tests.
        """

        # Only analyze test execution failures
        if report.when != "call":
            return

        if report.passed or report.skipped:
            return

        page = TestFailureHandler._get_page(item)

        page_url = ""

        if page:
            try:
                page_url = page.url
            except Exception:
                pass

        browser = TestFailureHandler._get_browser(item)

        screenshot = TestFailureHandler._capture_screenshot(
            page,
            item.name
        )

        error = call.excinfo.value

        stack_trace = "".join(
            traceback.format_exception(
                call.excinfo.type,
                call.excinfo.value,
                call.excinfo.tb
            )
        )

        context = FailureCollector.collect(
            test_name=item.name,
            error=error,
            stack_trace=stack_trace,
            page_url=page_url,
            browser=browser,
            screenshot_path=screenshot,
            timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )

        response = RootCauseAnalyzer.analyze(context)
        context.root_cause = response.response
        BugReportGenerator.generate(context)
