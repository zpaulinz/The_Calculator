import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from utils import display_error_message, display_success_message, display_warning_message
from io import StringIO

class TestErrorMessages(unittest.TestCase):

    def test_display_error_message(self):
        message = "Test error message"
        captured_output = StringIO()
        sys.stdout = captured_output

        display_error_message(message)

        sys.stdout = sys.__stdout__  # Reset redirect.
        self.assertIn("\033[31m", captured_output.getvalue())  # Check if RED color is in the output
        self.assertIn(message, captured_output.getvalue())  # Check if the message is displayed correctly

    def test_display_success_message(self):
        message = "Test success message"
        captured_output = StringIO()
        sys.stdout = captured_output

        display_success_message(message)

        sys.stdout = sys.__stdout__  # Reset redirect.
        self.assertIn("\033[32m", captured_output.getvalue())  # Check if GREEN color is in the output
        self.assertIn(message, captured_output.getvalue())  # Check if the message is displayed correctly

    def test_display_warning_message(self):
        message = "Test warning message"
        captured_output = StringIO()
        sys.stdout = captured_output

        display_warning_message(message)

        sys.stdout = sys.__stdout__  # Reset redirect.
        self.assertIn("\033[33m", captured_output.getvalue())  # Check if YELLOW color is in the output
        self.assertIn(message, captured_output.getvalue())  # Check if the message is displayed correctly

if __name__ == '__main__':
    unittest.main()
