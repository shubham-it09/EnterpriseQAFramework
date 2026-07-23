# """
# Module:
#     config_manager.py

# Description:
#     Loads and provides framework configuration.

# Author:
#     Shubham Pandey
# """

# from pathlib import Path

# from config.config_model import FrameworkConfig
# from config.yaml_reader import YamlReader


# class ConfigManager:
#     """
#     Responsible for loading and providing
#     framework configuration.
#     """

#     def __init__(self, environment: str = "qa") -> None:

#         self._environment = environment

#         self._reader = YamlReader()

#         self._config = self._load()

#     def _load(self) -> FrameworkConfig:
#         """
#         Loads configuration from YAML.
#         """

#         config_path = (
#             Path(__file__).parent
#             / "environments"
#             / f"{self._environment}.yaml"
#         )

#         return self._reader.read(config_path)

#     @property
#     def config(self) -> FrameworkConfig:
#         """
#         Returns framework configuration.
#         """

#         return self._config


# config = ConfigManager().config


from pathlib import Path

from config.yaml_reader import YamlReader


class ConfigManager:

    def __init__(self, environment: str = "qa"):

        config_path = (
            Path(__file__).parent
            / "environments"
            / f"{environment}.yaml"
        )

        self.reader = YamlReader()
        self.config = self.reader.read(config_path)

    @property
    def browser(self) -> str:
        return self.config.browser

    @property
    def base_url(self) -> str:
        return self.config.base_url

    @property
    def timeout(self) -> int:
        return self.config.timeout

    @property
    def headless(self) -> bool:
        return self.config.headless

    @property
    def slow_mo(self) -> int:
        return self.config.slow_mo
    
    @property
    def api_base_url(self) -> str:
        return self.config.api_base_url



config = ConfigManager()
print("base url **************************",config.base_url)
print("timeout******************************",config.timeout)