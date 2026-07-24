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