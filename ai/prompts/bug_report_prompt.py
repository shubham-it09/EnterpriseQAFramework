"""
==============================================================
Bug Report Prompt

Author : Shubham Pandey

Description
------------
Contains prompt used for generating AI Bug Reports.
==============================================================
"""


class BugReportPrompt:

    @staticmethod
    def build(context):
        return f"""
                You are a Senior QA Lead.

                Generate a professional bug report.

                Application URL:
                {context.page_url}

                Test Name:
                {context.test_name}

                Error:
                {context.error}

                Stack Trace:
                {context.stack_trace}

                AI Root Cause:
                {context.root_cause}

                Generate the report in this format.

                # Bug Summary

                # Environment

                # Steps to Reproduce

                # Expected Result

                # Actual Result

                # Root Cause

                # Suggested Fix

                # Severity

                # Priority
                """