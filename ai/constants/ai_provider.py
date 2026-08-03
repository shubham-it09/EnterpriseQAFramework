"""
==============================================================
AI Provider Enum

Author : Shubham Pandey

Description:
------------
Defines the list of AI providers supported by the framework.

Using an Enum avoids hard-coded strings throughout the codebase
and provides a type-safe way to identify AI providers.

Whenever a new AI provider is added, simply include it here
and implement its corresponding client.

Responsibilities:
-----------------
✓ Maintain the list of supported AI providers
✓ Eliminate hard-coded provider names
✓ Improve code readability and maintainability
==============================================================
"""

from enum import Enum


class AIProvider(Enum):
    """
    Enumeration of all supported AI providers.
    """

    OPENAI = "openai"

    GROQ = "groq"

    OLLAMA = "ollama"

    AZURE_OPENAI = "azure_openai"

    GEMINI = "gemini"