"""
==============================================================
Base AI Client

Author : Shubham Pandey

Description:
------------
Defines the contract that every AI provider must implement.

Examples:
    - OpenAI
    - Groq
    - Ollama
    - Azure OpenAI
    - Gemini

Any new AI provider can be integrated simply by implementing
this abstract base class.

Benefits:
---------
✓ Common interface for all AI providers
✓ Supports Factory Design Pattern
✓ Easy to extend
✓ Loosely coupled architecture
==============================================================
"""

from abc import ABC, abstractmethod

from ai.models.ai_request import AIRequest
from ai.models.ai_response import AIResponse


class BaseAIClient(ABC):
    """
    Abstract base class for all AI providers.

    This class defines the standard interface that every AI
    provider must follow.

    Every provider must implement the 'ask()' method.

    Example:

        OpenAIClient(BaseAIClient)

        GroqClient(BaseAIClient)

        OllamaClient(BaseAIClient)
    """

    @abstractmethod
    def ask(self, request: AIRequest) -> AIResponse:
        """
        Sends a request to the AI model and returns the response.

        Parameters
        ----------
        request : AIRequest
            Contains all information required to interact
            with the AI model.

        Returns
        -------
        AIResponse
            Standard response object returned by every AI provider.

        Notes
        -----
        Every AI provider must implement this method.
        """
        pass