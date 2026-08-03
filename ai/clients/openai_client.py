"""
==============================================================
OpenAI Client

Author : Shubham Pandey

Description:
------------
Implements the OpenAI provider.

Responsibilities
----------------
✓ Initialize OpenAI client
✓ Send prompt to OpenAI
✓ Convert provider response to AIResponse
==============================================================
"""

import time

from openai import OpenAI

from ai.clients.base_ai_client import BaseAIClient
from ai.models.ai_request import AIRequest
from ai.models.ai_response import AIResponse
from config.config_manager import config


class OpenAIClient(BaseAIClient):

    def __init__(self):
        """
        Initializes OpenAI client.
        """

        self.client = OpenAI(
            api_key=config.openai_api_key
        )

        self.model = config.openai_model

    def ask(self, request: AIRequest) -> AIResponse:

        start_time = time.perf_counter()

        try:

            response = self.client.chat.completions.create(

                model=self.model,

                messages=[
                    {
                        "role": "system",
                        "content": request.system_prompt or
                        "You are a helpful AI assistant."
                    },
                    {
                        "role": "user",
                        "content": request.prompt
                    }
                ],

                reasoning_effort="low",

                max_completion_tokens=8000
            )

            execution_time = round(
                time.perf_counter() - start_time,
                2
            )
            # print("\n================ RAW RESPONSE ================")
            # print(response)
            # print("==============================================")

            # print("\n================ CHOICE ======================")
            # print(response.choices[0])
            # print("==============================================")

            # print("\n================ MESSAGE =====================")
            # print(response.choices[0].message)
            # print("==============================================")

            return AIResponse(

                success=True,

                provider="OpenAI",

                model=self.model,

                response=response.choices[0].message.content,

                tokens=response.usage.total_tokens,

                execution_time=execution_time
            )

        except Exception as ex:

            return AIResponse(

                success=False,

                provider="OpenAI",

                model=self.model,

                response="",

                error=str(ex)
            )