"""
Module:
    config_manager.py

Description:
    Loads and provides framework configuration.

Author:
    Shubham Pandey
"""

from pathlib import Path

from config.config_model import FrameworkConfig
from config.yaml_reader import YamlReader


class ConfigManager:
    """
    Responsible for loading and providing
    framework configuration.
    """

    def __init__(self, environment: str = "qa") -> None:

        self._environment = environment

        self._reader = YamlReader()

        self._config = self._load()

    def _load(self) -> FrameworkConfig:
        """
        Loads configuration from YAML.
        """

        config_path = (
            Path(__file__).parent
            / "environments"
            / f"{self._environment}.yaml"
        )

        return self._reader.read(config_path)

    @property
    def config(self) -> FrameworkConfig:
        """
        Returns framework configuration.
        """

        return self._config


config = ConfigManager().config