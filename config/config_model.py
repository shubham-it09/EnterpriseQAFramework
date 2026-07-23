"""
Module:
    config_model.py

Description:
    Defines the strongly typed configuration model
    for the automation framework.

Author:
    Shubham Pandey
"""

from dataclasses import dataclass

@dataclass(frozen=True,slots=True)
class FrameworkConfig:
    """
    Immutable framework configuration.

    Attributes:
        environment: Active environment.
        base_url: Application URL.
        browser: Browser name.
        headless: Browser execution mode.
        timeout: Default timeout.
        slow_mo: Slow motion delay.
    """
    environment: str
    base_url: str
    browser: str
    headless: bool
    timeout: int
    slow_mo: int
    api_base_url: str