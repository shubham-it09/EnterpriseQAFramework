"""
==============================================================
Groq Client

Author : Shubham Pandey

Description:
------------
Implements the Groq AI provider.

Responsibilities
----------------
✓ Initialize Groq client
✓ Send prompt to Groq
✓ Convert provider response to AIResponse
==============================================================
"""

import time

from groq import Groq

from ai.clients.base_ai_client import BaseAIClient
from ai.models.ai_request import AIRequest
from ai.models.ai_response import AIResponse
from config.config_manager import config


class GroqClient(BaseAIClient):
    """
    Groq AI provider implementation.
    """

    def __init__(self):
        """
        Initializes Groq client.
        """

        self.client = Groq(
            api_key=config.groq_api_key
        )

        self.model = config.groq_model

    def ask(self, request: AIRequest) -> AIResponse:
        """
        Sends request to Groq AI.
        """

        start_time = time.perf_counter()

        try:

            response = self.client.chat.completions.create(

                model=self.model,

                messages=[
                    {
                        "role": "system",
                        "content": request.system_prompt
                        or "You are a helpful AI assistant."
                    },
                    {
                        "role": "user",
                        "content": request.prompt
                    }
                ],

                temperature=request.temperature,

                max_tokens=request.max_tokens
            )

            execution_time = round(
                time.perf_counter() - start_time,
                2
            )

            return AIResponse(

                success=True,

                provider="Groq",

                model=self.model,

                response=response.choices[0].message.content,

                tokens=response.usage.total_tokens,

                execution_time=execution_time
            )

        except Exception as ex:

            return AIResponse(

                success=False,

                provider="Groq",

                model=self.model,

                response="",

                error=str(ex)
            )