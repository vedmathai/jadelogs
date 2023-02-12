from tests.common import setup
from jadelogs.file_manager.file_manager import FileManager
from jadelogs import JadeLogger


def test_new_train_datapoint():
    setup()
    jade_logger = JadeLogger()
    jade_logger.new_experiment()
    jade_logger.new_epoch()
    jade_logger.new_train_batch()
    jade_logger.new_train_datapoint('a', 'b', {})
    file_manager = FileManager()
    log = file_manager.read_log_file()
    assert len(log.experiments()[0].epochs()[0].train_batches()[0].datapoints()) == 1

    # Test that it is creating the second datapoint when asked again
    jade_logger.new_train_datapoint('a', 'b', {})
    log = file_manager.read_log_file()
    assert len(log.experiments()[0].epochs()[0].train_batches()[0].datapoints()) == 2

    # Test that it is creating the datapoint in the lastest batch
    jade_logger.new_train_batch()
    jade_logger.new_train_datapoint('a', 'b', {})
    log = file_manager.read_log_file()
    assert len(log.experiments()[0].epochs()[0].train_batches()[1].datapoints()) == 1

def test_new_evaluate_datapoint():
    setup()
    jade_logger = JadeLogger()
    jade_logger.new_experiment()
    jade_logger.new_epoch()
    jade_logger.new_evaluate_batch()
    jade_logger.new_evaluate_datapoint('a', 'b', {})
    file_manager = FileManager()
    log = file_manager.read_log_file()
    assert len(log.experiments()[0].epochs()[0].evaluate_batches()[0].datapoints()) == 1

    # Test that it is creating the second datapoint when asked again
    jade_logger.new_evaluate_datapoint('a', 'b', {})
    log = file_manager.read_log_file()
    assert len(log.experiments()[0].epochs()[0].evaluate_batches()[0].datapoints()) == 2

    # Test that it is creating the datapoint in the lastest batch
    jade_logger.new_evaluate_batch()
    jade_logger.new_evaluate_datapoint('a', 'b', {})
    log = file_manager.read_log_file()
    assert len(log.experiments()[0].epochs()[0].evaluate_batches()[1].datapoints()) == 1

def test_new_test_datapoint():
    setup()
    jade_logger = JadeLogger()
    jade_logger.new_experiment()
    jade_logger.new_epoch()
    jade_logger.new_test_batch()
    jade_logger.new_test_datapoint('a', 'b', {})
    file_manager = FileManager()
    log = file_manager.read_log_file()
    assert len(log.experiments()[0].epochs()[0].test_batches()[0].datapoints()) == 1

    # Test that it is creating the second datapoint when asked again
    jade_logger.new_test_datapoint('a', 'b', {})
    log = file_manager.read_log_file()
    assert len(log.experiments()[0].epochs()[0].test_batches()[0].datapoints()) == 2

    # Test that it is creating the datapoint in the lastest batch
    jade_logger.new_test_batch()
    jade_logger.new_test_datapoint('a', 'b', {})
    log = file_manager.read_log_file()
    assert len(log.experiments()[0].epochs()[0].test_batches()[1].datapoints()) == 1
