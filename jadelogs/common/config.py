import json

CONFIG_DICT = {
    "project_folder": "jade_front"
}

class Config:
    _instance = None

    def __init__(self):
        self._project_folder = None

    @staticmethod
    def instantiate() -> None:
        if Config._instance is None:
            config = Config.from_dict(CONFIG_DICT)
            Config._instance = config

    @staticmethod
    def instance() -> "Config":
        if Config._instance is None:
            raise Exception('Config not instantiated, use Config.instantiate() function first')  # noqa
        return Config._instance

    def project_folder(self):
        return self._project_folder

    def set_project_folder(self, project_folder):
        self._project_folder = project_folder

    def to_dict(self):
        return {
            "project_folder": self.project_folder()
        }

    @staticmethod
    def from_dict(val):
        config = Config()
        config.set_project_folder(val["project_folder"])
        return config
