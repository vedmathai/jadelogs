from tests.common import setup
from jadelogs.file_manager.file_manager import FileManager
from jadelogs import JadeLogger


def test_new_epoch():
    setup()
    jade_logger = JadeLogger()
    jade_logger.new_experiment()
    jade_logger.new_epoch()
    file_manager = FileManager()
    log = file_manager.read_log_file()
    assert len(log.experiments()[0].epochs()) == 1

    # Test that it is creating the second epoch when asked again
    jade_logger.new_epoch()
    file_manager = FileManager()
    log = file_manager.read_log_file()
    assert len(log.experiments()[0].epochs()) == 2

    # Test that it is creating the epoch in the lastest experiment
    jade_logger.new_experiment()
    jade_logger.new_epoch()
    file_manager = FileManager()
    log = file_manager.read_log_file()
    assert len(log.experiments()[1].epochs()) == 1
