from jadelogs.common.config import Config
from jadelogs.file_manager.file_manager import FileManager
from jadelogs.datamodels.experiment_datamodel import ExperimentDatamodel
from jadelogs.datamodels.epoch_datamodel import EpochDatamodel
from jadelogs.datamodels.batch_datamodel import BatchDatamodel
from jadelogs.datamodels.datapoint_model import DatapointDatamodel
from jadelogs.datamodels.log_datamodel import LogDatamodel
from jadelogs.datamodels.jade_log_datamodel import JadeLogDatamodel


class JadeLogger:
    def __init__(self):
        self._jade_log = JadeLogDatamodel()
        self.file_manager = FileManager()
        config = Config.instantiate()

    def reset(self):
        self._jade_log = JadeLogDatamodel()

    def new_experiment(self):
        experiment = ExperimentDatamodel.create()
        self._jade_log.add_experiment(experiment)
        self.save_snapshot()

    def set_experiment_name(self, name):
        experiment = self._jade_log.current_experiment()
        experiment.set_name(name)

    def set_experiment_type(self, experiment_type):
        experiment = self._jade_log.current_experiment()
        experiment.set_experiment_type(experiment_type)

    def set_experiment_run_config(self, run_config):
        experiment = self._jade_log.current_experiment()
        experiment.set_run_config(run_config)

    def new_epoch(self):
        epoch = EpochDatamodel.create()
        current_experiment = self._jade_log.current_experiment()
        current_experiment.add_epoch(epoch)
        self.save_snapshot()

    def new_train_batch(self):
        self._new_batch('train')

    def new_evaluate_batch(self):
        self._new_batch('evaluate')

    def new_test_batch(self):
        self._new_batch('test')

    def new_train_datapoint(self, expected_label, predicted_label, loss, context):
        self._new_datapoint('train', expected_label, predicted_label, loss, context)

    def new_evaluate_datapoint(self, expected_label, predicted_label, loss, context):
        self._new_datapoint('evaluate', expected_label, predicted_label, loss, context)

    def new_test_datapoint(self, expected_label, predicted_label, loss, context):
        self._new_datapoint('test', expected_label, predicted_label, loss, context)

    def _new_batch(self, batch_type):
        experiment = self._jade_log.current_experiment()
        epoch = experiment.current_epoch()
        batch_type2fn = {
            'train': epoch.add_train_batch,
            'evaluate': epoch.add_evaluate_batch,
            'test': epoch.add_test_batch,
        }
        batch = BatchDatamodel.create()
        batch_type2fn[batch_type](batch)

    def _new_datapoint(self, batch_type, expected_label, predicted_label, loss, context):
        experiment = self._jade_log.current_experiment()
        epoch = experiment.current_epoch()
        batch_type2fn = {
            'train': epoch.current_train_batch,
            'evaluate': epoch.current_evaluate_batch,
            'test': epoch.current_test_batch,
        }
        batch = batch_type2fn[batch_type]()
        datapoint = DatapointDatamodel.create(expected_label, predicted_label, loss, context)
        batch.add_datapoint(datapoint)
        
    def end_experiment(self):
        self.save_snapshot()
        self.reset()

    def save_snapshot(self):
        self.file_manager.write_jade_log(self._jade_log)

    def from_snapshot(self, val):
        return JadeLogDatamodel.from_dict(val)

    def global_log(self, message, level=5):
        log = LogDatamodel.create(message, level)
        self._jade_log.add_global_log(log)
        self.save_snapshot()

    def log(self, message, level=5):
        experiment = self._jade_log.current_experiment()
        log = LogDatamodel.create(message, level)
        experiment.add_log(log)
        self.save_snapshot()

    def current_experiment(self):
        return self._jade_log.current_experiment()

    def current_epoch(self):
        return self.current_experiment().current_epoch()

    def set_total_epochs(self, total_epochs):
        experiment = self._jade_log.current_experiment()
        experiment.set_total_epochs(total_epochs)
