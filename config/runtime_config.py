import os


class RuntimeConfig:

    @property
    def environment(self) -> str | None:
        return os.getenv("ENVIRONMENT")

    @property
    def browser(self) -> str | None:
        return os.getenv("BROWSER")

    @property
    def headless(self) -> str | None:
        return os.getenv("HEADLESS")

    @property
    def ai_provider(self) -> str | None:
        """
        Returns AI provider supplied through runtime
        environment variables.

        Example:
            AI_PROVIDER=openai
        """
        return os.getenv("AI_PROVIDER")