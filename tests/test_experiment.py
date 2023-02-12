from tests.common import setup
from jadelogs.file_manager.file_manager import FileManager
from jadelogs import JadeLogger

  
def test_new_experiment():
    setup()
    jade_logger = JadeLogger()
    jade_logger.new_experiment()
    file_manager = FileManager()
    log = file_manager.read_log_file()
    assert len(log.experiments()) == 1

    # Test that it is creating the second experiment when asked again
    jade_logger.new_experiment()
    log = file_manager.read_log_file()
    assert len(log.experiments()) == 2
