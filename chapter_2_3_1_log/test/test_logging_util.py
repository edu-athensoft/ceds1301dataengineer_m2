import unittest
import logging
from chapter_2_3_1_log.util import logging_util

class TestLoggingUtil(unittest.TestCase):
    """
    Define a test class
    """
    # Define setUp and tearDown methods
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_init_logger(self):
        """
        Write a test case,
        Determine whether the object returned by the init_logger method is a logging object
        :return:
        """
        # Get the log object
        logger = logging_util.init_logger(None)
        # Determine whether the returned object is a logging object
        self.assertIsInstance(logger, logging.RootLogger)

        logger.info("chapter_2_3_1_log")
