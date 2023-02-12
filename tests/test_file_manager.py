import os

from tests.common import setup, PROJECT_ID
from jadelogs.file_manager.file_manager import FileManager
from jadelogs import JadeLogger


def test_file_manager():
    temp_folder = setup()
    file_manager = FileManager()
    original_data_filepath = os.path.join(
        temp_folder.name, PROJECT_ID, 'data', 'data.json'
    )
    data_filepath = file_manager.data_filepath('data.json')
    assert data_filepath == original_data_filepath
    code_filepath = file_manager.code_filepath('code.py')
    original_code_filepath = os.path.join(
        temp_folder.name, PROJECT_ID, 'code', 'code.py'
    )
    assert code_filepath == original_code_filepath
