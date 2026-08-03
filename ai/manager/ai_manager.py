"""
==============================================================
AI Manager

Author : Shubham Pandey

Description:
------------
Acts as the entry point for all AI interactions within the
framework.

AIManager delegates provider selection to LLMFactory and
request execution to the selected AI client.

Responsibilities:
-----------------
✓ Accept AI requests
✓ Obtain the configured AI client
✓ Execute the request
✓ Return the AI response
==============================================================
"""

from ai.factory.llm_factory import LLMFactory
from ai.models.ai_request import AIRequest
from ai.models.ai_response import AIResponse


class AIManager:
    """
    Entry point for all AI operations.
    """

    @staticmethod
    def ask(request: AIRequest) -> AIResponse:
        """
        Sends an AI request to the configured provider.

        Parameters
        ----------
        request : AIRequest
            Request object containing prompt and AI settings.

        Returns
        -------
        AIResponse
            Standardized AI response returned by the provider.
        """

        client = LLMFactory.get_client()

        return client.ask(request)