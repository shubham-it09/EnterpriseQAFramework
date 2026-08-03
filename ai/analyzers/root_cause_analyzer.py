"""
==============================================================
Root Cause Analyzer

Description:
------------
Analyzes Playwright test failures using AI and returns
a structured root cause analysis.
==============================================================
"""

from ai.manager.ai_manager import AIManager
from ai.models.ai_request import AIRequest
from ai.models.ai_response import AIResponse
from ai.collectors.failure_collector import FailureContext,FailureCollector
from ai.reporters.ai_report_writer import AIReportWriter


class RootCauseAnalyzer:
    """
    AI powered root cause analyzer.
    """

    @staticmethod
    def analyze(context: FailureContext) -> AIResponse:
        """
        Analyze a failed test.
        """

        prompt = f"""
                You are a Senior QA Automation Architect with expertise in:

                - Playwright
                - Selenium
                - API Automation
                - Python
                - CI/CD
                - Jenkins
                - Docker

                Analyze the following failed automation test.

                Test Name:
                {context.test_name}

                Browser:
                {context.browser}

                URL:
                {context.page_url}

                Error:
                {context.error}

                Stack Trace:
                {context.stack_trace}

                Screenshot:
                {context.screenshot_path}

                Console Logs:
                {context.console_logs}

                Network Logs:
                {context.network_logs}

                Provide the response using Markdown.

                ## Root Cause

                ## Possible Reason

                ## Suggested Fix

                ## Best Practice

                ## Confidence (0-100%)
                """

        request = AIRequest(prompt=prompt)
        response=AIManager.ask(request)


        AIReportWriter.write(
            context.test_name,
            response
            )
        return response