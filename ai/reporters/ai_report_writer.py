"""
==============================================================
AI Report Writer

Author : Shubham Pandey

Description
------------
Writes AI analysis into a Markdown report.

Responsibilities
----------------
✓ Create AI report folder
✓ Save AI analysis
✓ Return report path
==============================================================
"""

from pathlib import Path

from ai.models.ai_response import AIResponse


class AIReportWriter:
    """
    Writes AI reports.
    """

    REPORT_DIR = Path("artifacts/ai")

    @classmethod
    def write(
        cls,
        test_name: str,
        response: AIResponse
    ) -> str:

        cls.REPORT_DIR.mkdir(
            parents=True,
            exist_ok=True
        )

        report = cls.REPORT_DIR / f"{test_name}_root_cause.md"

        report.write_text(
            response.response,
            encoding="utf-8"
        )

        return str(report)