from datetime import datetime

from jadelogs.datamodels.batch_datamodel import BatchDatamodel


class EpochDatamodel:
    def __init__(self):
        self._start_time = None
        self._end_time = None
        self._train_batches = []
        self._evaluate_batches = []
        self._test_batches = []
        self._size = None
    
    def start_time(self):
        return self._start_time

    def end_time(self):
        return self._end_time

    def train_batches(self):
        return self._train_batches

    def current_train_batch(self):
        return self._train_batches[-1]

    def evaluate_batches(self):
        return self._evaluate_batches

    def current_evaluate_batch(self):
        return self._evaluate_batches[-1]

    def test_batches(self):
        return self._test_batches

    def current_test_batch(self):
        return self._test_batches[-1]

    def size(self):
        return self._size

    def set_start_time(self, start_time):
        self._start_time = start_time

    def set_end_time(self, end_time):
        self._end_time = end_time

    def set_train_batches(self, train_batches):
        self._train_batches = train_batches

    def add_train_batch(self, train_batch):
        self._train_batches.append(train_batch)

    def set_evaluate_batches(self, evaluate_batches):
        self._evaluate_batches = evaluate_batches

    def add_evaluate_batch(self, evaluate_batch):
        self._evaluate_batches.append(evaluate_batch)
    
    def set_test_batches(self, test_batches):
        self._test_batches = test_batches

    def add_test_batch(self, test_batch):
        self._test_batches.append(test_batch)

    def set_size(self, size):
        self._size = size

    @staticmethod
    def from_dict(val):
        epoch = EpochDatamodel()
        epoch.set_start_time(val['start_time'])
        epoch.set_end_time(val['end_time'])
        train_batches = [BatchDatamodel.from_dict(i) for i in val['train_batches']]
        evaluate_batches = [BatchDatamodel.from_dict(i) for i in val['evaluate_batches']]
        test_batches = [BatchDatamodel.from_dict(i) for i in val['test_batches']]
        epoch.set_train_batches(train_batches)
        epoch.set_evaluate_batches(evaluate_batches)
        epoch.set_test_batches(test_batches)
        epoch.set_size(val['size'])
        return epoch

    @staticmethod
    def create():
        epoch = EpochDatamodel()
        epoch.set_start_time(str(datetime.utcnow().timestamp()))
        return epoch

    def to_dict(self):
        return {
            'start_time': self.start_time(),
            'end_time': self.end_time(),
            'train_batches': [i.to_dict() for i in self.train_batches()],
            'evaluate_batches': [i.to_dict() for i in self.evaluate_batches()],
            'test_batches': [i.to_dict() for i in self.test_batches()],
            'size': self.size(),
        }
