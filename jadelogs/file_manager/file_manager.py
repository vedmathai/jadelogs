import json
import os

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

    def logs_filepath(self):
        request_id = self.request_id()
        folderpath = os.path.join(self.project_folder(), request_id)
        if not os.path.exists(folderpath):
            os.makedirs(folderpath)
        return folderpath

    def write_jade_log(self, jade_log):
        folderpath = self.logs_filepath()
        filepath = os.path.join(folderpath, 'log.json')
        with open(filepath, 'wt') as f:
            json.dump(jade_log.to_dict(), f)

    def read_log_file(self):
        folderpath = self.logs_filepath()
        filepath = os.path.join(folderpath, 'log.json')
        with open(filepath, 'rt') as f:
            jade_log = JadeLogDatamodel.from_dict(json.load(f))
        return jade_log
