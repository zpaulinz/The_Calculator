import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from unittest.mock import patch
from user_input import get_user_choice, get_numbers_for_operation

class TestUserInput(unittest.TestCase):

    @patch('builtins.input', return_value='1')
    def test_get_user_choice_valid(self, mock_input):
        operations = {'1': ('Add', None), '2': ('Subtract', None)}
        result = get_user_choice(operations)
        self.assertEqual(result, '1')

    @patch('builtins.input', return_value='0')
    def test_get_user_choice_exit(self, mock_input):
        operations = {'1': ('Add', None), '2': ('Subtract', None)}
        result = get_user_choice(operations)
        self.assertEqual(result, '0')

    @patch('builtins.input', side_effect=['3', '2'])  
    def test_get_user_choice_invalid(self, mock_input):
        operations = {'1': ('Add', None), '2': ('Subtract', None)}
        result = get_user_choice(operations)
        self.assertEqual(result, '2')

    @patch('builtins.input', side_effect=['5', '2'])  
    def test_get_user_choice_invalid_input(self, mock_input):
        operations = {'1': ('Add', None), '2': ('Subtract', None)}
        result = get_user_choice(operations)
        self.assertEqual(result, '2')

    @patch('builtins.input', side_effect=['10', '5'])
    def test_get_numbers_for_operation(self, mock_input):
        result = get_numbers_for_operation()
        self.assertEqual(result, (10.0, 5.0))

if __name__ == '__main__':
    unittest.main()