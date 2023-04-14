from datetime import datetime


from jadelogs.datamodels.epoch_datamodel import EpochDatamodel
from jadelogs.datamodels.log_datamodel import LogDatamodel


class ExperimentDatamodel:
    def __init__(self):
        self._name = None
        self._experiment_type = None
        self._start_time = None
        self._end_time = None
        self._id = None
        self._run_config = None
        self._total_epochs = None
        self._epochs = []
        self._logs = []
    
    def id(self):
        return self._id
    
    def name(self):
        return self._name
    
    def experiment_type(self):
        return self._experiment_type

    def start_time(self):
        return self._start_time

    def end_time(self):
        return self._end_time

    def epochs(self):
        return self._epochs

    def total_epochs(self):
        return self._total_epochs

    def run_config(self):
        return self._run_config

    def current_epoch(self):
        return self._epochs[-1]

    def logs(self):
        return self._logs

    def set_id(self, id):
        self._id = id

    def set_name(self, name):
        self._name = name

    def set_experiment_type(self, experiment_type):
        self._experiment_type = experiment_type

    def set_start_time(self, start_time):
        self._start_time = start_time

    def set_end_time(self, end_time):
        self._end_time = end_time

    def set_epochs(self, epochs):
        self._epochs = epochs

    def set_total_epochs(self, total_epochs):
        self._total_epochs = total_epochs

    def set_run_config(self, run_config):
        self._run_config = run_config

    def set_logs(self, logs):
        self._logs = logs

    def add_log(self, log):
        self._logs.append(log)

    def add_epoch(self, epoch):
        self._epochs.append(epoch)

    @staticmethod
    def from_dict(val):
        experiment = ExperimentDatamodel()
        experiment.set_name(val['name'])
        experiment.set_experiment_type(val['experiment_type'])
        experiment.set_start_time(val['start_time'])
        experiment.set_end_time(val['end_time'])
        epochs = [EpochDatamodel.from_dict(i) for i in val['epochs']]
        experiment.set_epochs(epochs)
        experiment.set_total_epochs(val['total_epochs'])
        experiment.set_run_config(val['run_config'])
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
            'name': self.name(),
            'experiment_type': self.experiment_type(),
            'start_time': self.start_time(),
            'end_time': self.end_time(),
            'epochs': [i.to_dict() for i in self.epochs()],
            'total_epochs': self.total_epochs(),
            'run_config': self.run_config(),
            'logs': [i.to_dict() for i in self.logs()],
        }
