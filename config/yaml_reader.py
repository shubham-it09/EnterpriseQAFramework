"""
Module:
    yaml_reader.py

Description:
    Reads YAML configuration files and converts them
    into FrameworkConfig objects.

Author:
    Shubham Pandey
"""

from pathlib import Path

import yaml

from config.config_model import FrameworkConfig


class YamlReader:
    """
    Responsible for reading YAML configuration files.
    """

    def read(self, file_path: Path) -> FrameworkConfig:
        """
        Reads a YAML file and converts it into
        a FrameworkConfig object.

        Args:
            file_path: Path of the YAML file.

        Returns:
            FrameworkConfig
        """

        with file_path.open(
            mode="r",
            encoding="utf-8"
        ) as stream:

            data = yaml.safe_load(stream)

        return FrameworkConfig(**data)