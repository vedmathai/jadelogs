from datetime import datetime

from jadelogs.datamodels.log_datamodel import LogDatamodel
from jadelogs.datamodels.experiment_datamodel import ExperimentDatamodel



class JadeLogDatamodel:
    def __init__(self):
        self._global_logs = []
        self._experiments = []

    def global_logs(self):
        return self._global_logs

    def experiments(self):
        return self._experiments

    def current_experiment(self):
        return self._experiments[-1]

    def set_global_logs(self, global_logs):
        self._global_logs = global_logs

    def set_experiments(self, experiments):
        self._experiments = experiments

    def add_global_log(self, global_log):
        self._global_logs.append(global_log)

    def add_experiment(self, experiment):
        self._experiments.append(experiment)

    @staticmethod
    def from_dict(val):
        jadelog = JadeLogDatamodel()
        experiments = [ExperimentDatamodel.from_dict(i) for i in val['experiments']]
        jadelog.set_experiments(experiments)
        global_logs = [LogDatamodel.from_dict(i) for i in val['global_logs']]
        jadelog.set_global_logs(global_logs)
        return jadelog

    @staticmethod
    def create(self):
        return JadeLogDatamodel()

    def to_dict(self):
        return {
            "global_logs": [i.to_dict() for i in self.global_logs()],
            "experiments": [i.to_dict() for i in self.experiments()],
        }
