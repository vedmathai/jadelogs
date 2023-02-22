class DatapointDatamodel:
    def __init__(self):
        self._expected_label = None
        self._predicted_label = None
        self._loss = None
        self._context = None

    def expected_label(self):
        return self._expected_label

    def predicted_label(self):
        return self._predicted_label

    def loss(self):
        return self._loss

    def context(self):
        return self._context

    def set_expected_label(self, expected_label):
        self._expected_label = expected_label

    def set_predicted_label(self, predicted_label):
        self._predicted_label = predicted_label

    def set_loss(self, loss):
        self._loss = loss

    def set_context(self, context):
        self._context = context

    @staticmethod
    def from_dict(val):
        datapoint = DatapointDatamodel()
        datapoint.set_expected_label(val['expected_label'])
        datapoint.set_predicted_label(val['predicted_label'])
        datapoint.set_loss(val['loss'])
        datapoint.set_context(val['context'])
        return datapoint

    @staticmethod
    def create(expected_label, predicted_label, loss, context):
        datapoint = DatapointDatamodel()
        datapoint.set_expected_label(expected_label)
        datapoint.set_predicted_label(predicted_label)
        datapoint.set_loss(loss)
        datapoint.set_context(context)
        return datapoint

    def to_dict(self):
        return {
            'expected_label': self.expected_label(),
            'predicted_label': self.predicted_label(),
            'loss': self.loss(),
            'context': self.context(),
        }
