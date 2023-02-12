import os
import json
from tempfile import TemporaryDirectory

from jadelogs.common.config import Config


PROJECT_ID = "__123_PROJECT_ID_123__"
REQUEST_ID = "__123_REQUEST_ID_123__"

def setup():
    Config.instantiate()
    config = Config.instance()
    temp_folder = TemporaryDirectory()
    config.set_project_folder(temp_folder.name)
    os.environ["PROJECT_ID"] = PROJECT_ID
    os.environ["REQUEST_ID"] = REQUEST_ID
    return temp_folder
