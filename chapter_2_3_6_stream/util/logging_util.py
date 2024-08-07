"""
LoggingUtil Tool Class
"""
import logging
from chapter_2_3_6_stream.config import project_config as conf

class LoggingUtil(object):
    # 获得logger对象
    def __init__(self, name=None, level=logging.INFO):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)


def init_logger(name=None):
    """
    Initializing an object
    :param name:
    :return:
    """
    # Creating a log object
    logger = LoggingUtil(name).logger
    # Creating Terminal Output
    console_handler = logging.StreamHandler()
    # Creating a Log Processor
    file_handler = logging.FileHandler(
        filename=conf.log_path + conf.log_name,
        mode='a',
        encoding='utf-8'
    )
    # Set the log output format
    formatter = logging.Formatter('%(asctime)s - [%(levelname)s] - %(filename)s[%(lineno)d]：%(message)s')
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)
    # Bind a log handler to a log object
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger
