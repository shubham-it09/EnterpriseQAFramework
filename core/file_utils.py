"""
Module:
    file_utils.py

Description:
    Utility methods for reading framework files.

Author:
    Shubham Pandey
"""

import json
from pathlib import Path


class FileUtils:

    @staticmethod
    def read_json(file_path: str | Path) -> dict:
        """
        Reads JSON file and returns dictionary.
        """

        file_path = Path(file_path)

        with file_path.open(
            mode="r",
            encoding="utf-8"
        ) as file:

            return json.load(file)