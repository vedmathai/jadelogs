from datetime import datetime


from jadelogs.datamodels.datapoint_model import DatapointDatamodel


class BatchDatamodel:
    def __init__(self):
        self._start_time = None
        self._end_time = None
        self._datapoints = []
    
    def start_time(self):
        return self._start_time

    def end_time(self):
        return self._end_time

    def datapoints(self):
        return self._datapoints

    def set_start_time(self, start_time):
        self._start_time = start_time

    def set_end_time(self, end_time):
        self._end_time = end_time

    def set_datapoints(self, datapoints):
        self._datapoints = datapoints

    def add_datapoint(self, datapoint):
        self._datapoints.append(datapoint)

    @staticmethod
    def from_dict(val):
        batch = BatchDatamodel()
        batch.set_start_time(val['start_time'])
        batch.set_end_time(val['end_time'])
        datapoints = [DatapointDatamodel.from_dict(i) for i in val['datapoints']]
        batch.set_datapoints(datapoints)
        return batch

    @staticmethod
    def create():
        experiment = BatchDatamodel()
        experiment.set_start_time(str(datetime.utcnow().timestamp()))
        return experiment

    def to_dict(self):
        return {
            'start_time': self.start_time(),
            'end_time': self.end_time(),
            'datapoints': [i.to_dict() for i in self.datapoints()]
        }
