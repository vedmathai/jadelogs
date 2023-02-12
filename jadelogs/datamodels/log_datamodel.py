from datetime import datetime


class LogDatamodel:
    def __init__(self):
        self._level = None
        self._message = ""
        self._time = None

    def level(self):
        return self._level

    def message(self):
        return self._message

    def time(self):
        return self._time

    def set_level(self, level):
        self._level = level

    def set_message(self, message):
        self._message = message

    def set_time(self, time):
        self._time = time

    @staticmethod
    def from_dict(val):
        log = LogDatamodel()
        log.set_level(val['level'])
        log.set_message(val['message'])
        log.set_time(val['time'])
        return log

    @staticmethod
    def create(message, level):
        log = LogDatamodel()
        log.set_level(level)
        log.set_message(message)
        log.set_time(str(datetime.utcnow().timestamp()))
        return log

    def to_dict(self):
        return {
            'level': self.level(),
            'message': self.message(),
            'time': self.time(),
        }
