import os

from tests.common import setup, PROJECT_ID
from jadelogs.file_manager.file_manager import FileManager
from jadelogs import JadeLogger


def test_file_manager():
    temp_folder = setup()
    file_manager = FileManager()
    original_data_folderpath = os.path.join(
        temp_folder.name, PROJECT_ID, 'data'
    )
    original_data_filepath = os.path.join(
        original_data_folderpath, 'data.json'
    )
    os.makedirs(original_data_folderpath)
    with open(original_data_filepath, 'wt') as f:
        f.write('datavalue')
    data_filepath = file_manager.data_filepath('data.json')
    with open(data_filepath, 'rt') as f:
        assert f.read() == 'datavalue'
    assert data_filepath == original_data_filepath
    code_filepath = file_manager.code_filepath('code.py')
    original_code_filepath = os.path.join(
        temp_folder.name, PROJECT_ID, 'code', 'code.py'
    )
    assert code_filepath == original_code_filepath
    data_files = file_manager.list_data_dir('.')
    data_files = ['/'.join(i.split('/')[3:]) for i in data_files]
    assert data_files == ['__123_PROJECT_ID_123__/data/./data.json']
