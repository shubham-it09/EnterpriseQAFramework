"""
==============================================================
AI Request Model

Author : Shubham Pandey

Description:
------------
Represents a request sent to an AI model.

This class acts as a Data Transfer Object (DTO) and contains
all the information required by an AI provider to process
a request.

Every AI provider (OpenAI, Groq, Ollama, etc.) receives the
same request object, ensuring a consistent interface across
the framework.

Responsibilities:
-----------------
✓ Store AI request data
✓ Standardize communication between framework and AI providers
✓ Keep provider implementations independent
==============================================================
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class AIRequest:
    """
    Represents a standardized AI request.

    This object contains all the inputs required by an AI model
    to generate a response.
    """

    # User prompt sent to the AI model.
    prompt: str

    # Optional system instruction that defines the AI's behavior.
    system_prompt: Optional[str] = None

    # Optional image path for vision-capable AI models.
    image_path: Optional[str] = None

    # Controls randomness.
    # Lower value = More deterministic responses.
    # Higher value = More creative responses.
    temperature: float = 0.2

    # Maximum number of tokens the AI is allowed to generate.
    max_tokens: int = 1500

