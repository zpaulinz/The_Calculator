import unittest
from unittest.mock import patch
from user_input import get_float_input

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

if __name__ == "__main__":
    unittest.main()
