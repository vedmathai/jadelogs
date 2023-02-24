import json
import os
import shutil

from jadelogs.common.config import Config
from jadelogs.datamodels.jade_log_datamodel import JadeLogDatamodel


class FileManager:

    def project_folder(self):
        project_id = os.environ['PROJECT_ID']
        project_folder = os.path.join(
            Config.instance().project_folder(),
            project_id,
        )
        return project_folder

    def code_folder(self):
        return os.path.join(self.project_folder(), 'code')

    def data_folder(self):
        return os.path.join(self.project_folder(), 'data')

    def logs_folder(self):
        return os.path.join(self.project_folder(), 'logs')

    def data_filepath(self, filepath):
        filepath = os.path.join(self.data_folder(), filepath)
        return filepath

    def code_filepath(self, filepath):
        filepath = os.path.join(self.code_folder(), filepath)
        return filepath

    def request_id(self):
        request_id = os.environ['REQUEST_ID']
        return request_id

    def logs_folderpath(self):
        request_id = self.request_id()
        folderpath = os.path.join(self.project_folder(), 'logs', request_id)
        if not os.path.exists(folderpath):
            os.makedirs(folderpath)
        return folderpath

    def write_jade_log(self, jade_log):
        folderpath = self.logs_folderpath()
        inner_folderpath = os.path.join(folderpath, 'logs')
        if os.path.exists(inner_folderpath) is False:
            os.makedirs(inner_folderpath)
        filepath = os.path.join(inner_folderpath, 'log.json')
        with open(filepath, 'wt') as f:
            json.dump(jade_log.to_dict(), f)
        shutil.make_archive(inner_folderpath, 'zip', inner_folderpath)

    def read_log_file(self):
        folderpath = self.logs_folderpath()
        filepath = os.path.join(folderpath, 'log.json')
        with open(filepath, 'rt') as f:
            jade_log = JadeLogDatamodel.from_dict(json.load(f))
        return jade_log

    def list_data_dir(self, relative_data_dir):
        folder_path = os.path.join(self.data_folder(), relative_data_dir)
        files = os.listdir(folder_path)
        files = [os.path.join(folder_path, i) for i in files]
        return files
