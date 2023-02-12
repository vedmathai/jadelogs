from datetime import datetime


from jadelogs.datamodels.epoch_datamodel import EpochDatamodel
from jadelogs.datamodels.log_datamodel import LogDatamodel


class ExperimentDatamodel:
    def __init__(self):
        self._start_time = None
        self._end_time = None
        self._id = None
        self._config = None
        self._epochs = []
        self._logs = []
    
    def id(self):
        return self._id

    def start_time(self):
        return self._start_time

    def end_time(self):
        return self._end_time

    def epochs(self):
        return self._epochs

    def config(self):
        return self._config

    def current_epoch(self):
        return self._epochs[-1]

    def logs(self):
        return self._logs

    def set_id(self, id):
        self._id = id

    def set_start_time(self, start_time):
        self._start_time = start_time

    def set_end_time(self, end_time):
        self._end_time = end_time

    def set_epochs(self, epochs):
        self._epochs = epochs

    def set_config(self, config):
        self._config = config

    def set_logs(self, logs):
        self._logs = logs

    def add_log(self, log):
        self._logs.append(log)

    def add_epoch(self, epoch):
        self._epochs.append(epoch)

    @staticmethod
    def from_dict(val):
        experiment = ExperimentDatamodel()
        experiment.set_start_time(val['start_time'])
        experiment.set_end_time(val['end_time'])
        epochs = [EpochDatamodel.from_dict(i) for i in val['epochs']]
        experiment.set_epochs(epochs)
        experiment.set_config(val['config'])
        logs = [LogDatamodel.from_dict(i) for i in val['logs']]
        experiment.set_logs(logs)
        return experiment

    @staticmethod
    def create():
        experiment = ExperimentDatamodel()
        experiment.set_start_time(str(datetime.utcnow().timestamp()))
        return experiment

    def to_dict(self):
        return {
            'start_time': self.start_time(),
            'end_time': self.end_time(),
            'epochs': [i.to_dict() for i in self.epochs()],
            'config': self.config(),
            'logs': [i.to_dict() for i in self.logs()],
        }
