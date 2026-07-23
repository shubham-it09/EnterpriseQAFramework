"""
Module:
    logger_manager.py

Description:
    Creates and manages loggers for test execution.

Author:
    Shubham Pandey
"""

import logging
from pathlib import Path
from core.artifact_manager import ArtifactManager


class LoggerManager:

    @staticmethod
    def get_logger(test_name: str) -> logging.Logger:

        log_folder = ArtifactManager.get_logs_folder()
        log_folder.mkdir(exist_ok=True)

        logger = logging.getLogger(test_name)

        logger.setLevel(logging.INFO)
        logger.propagate = False

        if not logger.handlers:

            file_handler = logging.FileHandler(
                log_folder / f"{test_name}.log",
                mode="w",
                encoding="utf-8"
            )

            formatter = logging.Formatter(
                "%(asctime)s | %(levelname)-8s | %(filename)s:%(lineno)d | %(message)s"
            )

            file_handler.setFormatter(formatter)

            logger.addHandler(file_handler)

        return logger