from pathlib import Path

from ai.manager.ai_manager import AIManager
from ai.models.ai_request import AIRequest
from ai.prompts.bug_report_prompt import BugReportPrompt


class BugReportGenerator:

    REPORT_DIR = Path("artifacts/bugs")

    @classmethod
    def generate(cls, context):

        cls.REPORT_DIR.mkdir(
            parents=True,
            exist_ok=True
        )

        prompt = BugReportPrompt.build(context)

        response = AIManager.ask(
            AIRequest(prompt=prompt)
        )

        if response.success:

            report = (
                cls.REPORT_DIR /
                f"{context.test_name}_bug_report.md"
            )

            report.write_text(
                response.response,
                encoding="utf-8"
            )

        return response