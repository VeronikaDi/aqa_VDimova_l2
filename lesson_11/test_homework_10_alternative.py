import unittest

from lesson_11.homework_10 import log_event


def read_last_log_message():
    with open('login_system.log', 'r') as file:
        lines = file.readlines()
    return lines[-1].strip()


class TestLogEvent(unittest.TestCase):

    def test_log_success(self):
        log_event("User_1", "success")
        log_message = read_last_log_message()
        expected_message = "Login event - Username: User_1, Status: success"
        self.assertIn(expected_message, log_message)

    def test_log_expired(self):
        log_event("User_2", "expired")
        log_message = read_last_log_message()
        expected_message = "Login event - Username: User_2, Status: expired"
        self.assertIn(expected_message, log_message)

    def test_log_failed(self):
        log_event("User_3", "failed")
        log_message = read_last_log_message()
        expected_message = "Login event - Username: User_3, Status: failed"
        self.assertIn(expected_message, log_message)


if __name__ == '__main__':
    unittest.main()
