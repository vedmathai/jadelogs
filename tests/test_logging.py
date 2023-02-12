from tests.common import setup
from jadelogs.file_manager.file_manager import FileManager
from jadelogs import JadeLogger


def test_global_logs():
    setup()
    jade_logger = JadeLogger()
    jade_logger.global_log('log_message', level=5)
    file_manager = FileManager()
    log = file_manager.read_log_file()
    assert len(log.global_logs()) == 1

    # Test that it is creating the second log when asked again
    jade_logger.global_log('log_message', level=5)
    log = file_manager.read_log_file()
    assert len(log.global_logs()) == 2


def test_experiment_logs():
    setup()
    jade_logger = JadeLogger()
    jade_logger.new_experiment()
    jade_logger.log('log_message', level=5)
    file_manager = FileManager()
    log = file_manager.read_log_file()
    assert len(log.experiments()[0].logs()) == 1

    # Test that it is creating the second experiment when asked again
    jade_logger.log('log_message', level=5)
    log = file_manager.read_log_file()
    assert len(log.experiments()[0].logs()) == 2

    # Test that it is creating the second experiment when asked again
    jade_logger.new_experiment()
    jade_logger.log('log_message', level=5)
    log = file_manager.read_log_file()
    assert len(log.experiments()[1].logs()) == 1
