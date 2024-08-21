import unittest
from unittest.mock import patch
import logging

from lesson_11.homework_10 import log_event


class TestLogEvent(unittest.TestCase):

    @patch('logging.getLogger')
    @patch('logging.basicConfig')
    def test_log_success(self, mock_basicConfig, mock_getLogger):
        mock_logger = mock_getLogger.return_value
        log_event("User_1", "success")
        mock_logger.info.assert_called_with("Login event - Username: User_1, Status: success")

    @patch('logging.getLogger')
    @patch('logging.basicConfig')
    def test_log_expired(self, mock_basicConfig, mock_getLogger):
        mock_logger = mock_getLogger.return_value
        log_event("User_2", "expired")
        mock_logger.warning.assert_called_with("Login event - Username: User_2, Status: expired")

    @patch('logging.getLogger')
    @patch('logging.basicConfig')
    def test_log_failed(self, mock_basicConfig, mock_getLogger):
        mock_logger = mock_getLogger.return_value
        log_event("User_3", "failed")
        mock_logger.error.assert_called_with("Login event - Username: User_3, Status: failed")


if __name__ == '__main__':
    unittest.main()
