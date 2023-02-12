from tests.common import setup
from jadelogs.file_manager.file_manager import FileManager
from jadelogs import JadeLogger


def test_new_train_batch():
    setup()
    jade_logger = JadeLogger()
    jade_logger.new_experiment()
    jade_logger.new_epoch()
    jade_logger.new_train_batch()
    file_manager = FileManager()
    log = file_manager.read_log_file()
    assert len(log.experiments()[0].epochs()[0].train_batches()) == 1

    # Test that it is creating the test batch epoch when asked again
    jade_logger.new_train_batch()
    log = file_manager.read_log_file()
    assert len(log.experiments()[0].epochs()[0].train_batches()) == 2

    # Test that it is creating the test batch in the lastest epoch
    jade_logger.new_epoch()
    jade_logger.new_train_batch()
    log = file_manager.read_log_file()
    assert len(log.experiments()[0].epochs()[1].train_batches()) == 1

def test_new_evaluate_batch():
    setup()
    jade_logger = JadeLogger()
    jade_logger.new_experiment()
    jade_logger.new_epoch()
    jade_logger.new_evaluate_batch()
    file_manager = FileManager()
    log = file_manager.read_log_file()
    assert len(log.experiments()[0].epochs()[0].evaluate_batches()) == 1

    # Test that it is creating the test batch epoch when asked again
    jade_logger.new_evaluate_batch()
    log = file_manager.read_log_file()
    assert len(log.experiments()[0].epochs()[0].evaluate_batches()) == 2

    # Test that it is creating the test batch in the lastest epoch
    jade_logger.new_epoch()
    jade_logger.new_evaluate_batch()
    log = file_manager.read_log_file()
    assert len(log.experiments()[0].epochs()[1].evaluate_batches()) == 1

def test_new_test_batch():
    setup()
    jade_logger = JadeLogger()
    jade_logger.new_experiment()
    jade_logger.new_epoch()
    jade_logger.new_test_batch()
    file_manager = FileManager()
    log = file_manager.read_log_file()
    assert len(log.experiments()[0].epochs()[0].test_batches()) == 1

    # Test that it is creating the test batch epoch when asked again
    jade_logger.new_test_batch()
    log = file_manager.read_log_file()
    assert len(log.experiments()[0].epochs()[0].test_batches()) == 2

    # Test that it is creating the test batch in the lastest epoch
    jade_logger.new_epoch()
    jade_logger.new_test_batch()
    log = file_manager.read_log_file()
    assert len(log.experiments()[0].epochs()[1].test_batches()) == 1
