import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from unittest.mock import patch
from io import StringIO

from user_input import get_float_input, display_operations


class TestGetFloatInput(unittest.TestCase):
    @patch('builtins.input', side_effect=["abc", "3.14"])
    def test_get_float_input_invalid_then_valid(self, mock_input):
        result = get_float_input("Enter a number: ")
        self.assertEqual(result, 3.14)

    @patch('builtins.input', side_effect=["12.34"])  
    def test_get_float_input_valid(self, mock_input):
        result = get_float_input("Enter a number: ")
        self.assertEqual(result, 12.34)
    
    @patch('builtins.input', side_effect=["hello", "42"])  
    def test_get_float_input_text_then_number(self, mock_input):
        result = get_float_input("Enter a number: ")
        self.assertEqual(result, 42)

    @patch('builtins.input', side_effect=["", "42"])  
    def test_get_float_input_empty_then_number(self, mock_input):
        result = get_float_input("Enter a number: ")
        self.assertEqual(result, 42)

class TestDisplayOperations(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_display_operations(self, mock_stdout):
        operations = {
            '1': {'name': 'Add'},
            '2': {'name': 'Subtract'},
            '3': {'name': 'Multiply'},
            '4': {'name': 'Divide'},
            '5': {'name': 'Exponentiation'}
        }
        display_operations(operations)  
        output = mock_stdout.getvalue().strip()
        expected_output = (
            "Available operations:\n"
            "1. Add\n"
            "2. Subtract\n"
            "3. Multiply\n"
            "4. Divide\n"
            "5. Exponentiation\n"
            "0. Exit"
        )
        self.assertEqual(output, expected_output)


if __name__ == "__main__":
    unittest.main()
