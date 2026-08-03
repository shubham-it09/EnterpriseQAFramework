"""
==============================================================
Failure Collector

Description
-----------
Collects execution details from failed Playwright tests.
==============================================================
"""

from dataclasses import dataclass


from dataclasses import dataclass


@dataclass(slots=True)
class FailureContext:
    """
    Stores all failure information collected from a failed test.
    """

    test_name: str
    error: str
    stack_trace: str

    page_url: str = ""
    browser: str = ""

    screenshot_path: str = ""
    trace_path: str = ""
    video_path: str = ""

    console_logs: str = ""
    network_logs: str = ""

    timestamp: str = ""


class FailureCollector:

    @staticmethod
    def collect(
        test_name: str,
        error: Exception,
        stack_trace: str,
        page_url: str = "",
        browser: str = "",
        screenshot_path: str = "",
        trace_path: str = "",
        video_path: str = "",
        console_logs: str = "",
        network_logs: str = "",
        timestamp: str = "",
    ) -> FailureContext:

        return FailureContext(
            test_name=test_name,
            error=str(error),
            stack_trace=stack_trace,
            page_url=page_url,
            browser=browser,
            screenshot_path=screenshot_path,
            trace_path=trace_path,
            video_path=video_path,
            console_logs=console_logs,
            network_logs=network_logs,
            timestamp=timestamp,
        )