"""
==============================================================
LLM Factory

Author : Shubham Pandey

Description:
------------
Factory class responsible for creating the appropriate AI client
based on the configured AI provider.

The rest of the framework never creates AI clients directly.
Instead, every component requests a client from this factory.

Responsibilities:
-----------------
✓ Read configured AI provider
✓ Return appropriate AI client
✓ Hide provider creation logic from callers
==============================================================
"""

from ai.clients.groq_client import GroqClient
# from ai.clients.ollama_client import OllamaClient
from ai.clients.openai_client import OpenAIClient
from ai.constants.ai_provider import AIProvider
from config.config_manager import ConfigManager,config


class LLMFactory:
    """
    Factory responsible for creating AI client instances.
    """

    @staticmethod
    def get_client():
        """
        Returns the configured AI client.

        Returns
        -------
        BaseAIClient
            Instance of the configured AI provider.

        Raises
        ------
        ValueError
            If the configured provider is not supported.
        """

        provider = config.ai_provider

        if provider == AIProvider.OPENAI.value:
            return OpenAIClient()

        if provider == AIProvider.GROQ.value:
            return GroqClient()

        if provider == AIProvider.OLLAMA.value:
            return OllamaClient()

        raise ValueError(f"Unsupported AI Provider : {provider}")