import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from unittest.mock import patch
from io import StringIO
from main import main

class TestCalculatorMenu(unittest.TestCase):

    @patch('builtins.input', side_effect=['1', '2', '3', '5'])  
    @patch('sys.stdout', new_callable=StringIO)
    def test_calculator_full_cycle(self, mock_stdout, mock_input):
        main()  
        
        output = mock_stdout.getvalue()

        self.assertIn("The result is: 5.0", output)
        self.assertIn("Exit", output)  

    @patch('builtins.input', side_effect=['2', '5', '3', '5'])  
    @patch('sys.stdout', new_callable=StringIO)
    def test_calculator_subtraction(self, mock_stdout, mock_input):
        main()
        output = mock_stdout.getvalue()

        self.assertIn("The result is: 2.0", output) 
        self.assertIn("Exit", output)

    @patch('builtins.input', side_effect=['3', '4', '6', '5'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_calculator_multiplication(self, mock_stdout, mock_input):
        main()
        output = mock_stdout.getvalue()

        self.assertIn("The result is: 24.0", output)
        self.assertIn("Exit", output) 

    @patch('builtins.input', side_effect=['4', '6', '2', '5']) 
    @patch('sys.stdout', new_callable=StringIO)
    def test_calculator_division(self, mock_stdout, mock_input):
        main()
        output = mock_stdout.getvalue()

        self.assertIn("The result is: 3.0", output) 
        self.assertIn("Exit", output) 

    @patch('builtins.input', side_effect=['5']) 
    @patch('sys.stdout', new_callable=StringIO)
    def test_calculator_exit(self, mock_stdout, mock_input):
        main()
        output = mock_stdout.getvalue()

        self.assertIn("Exit", output)

if __name__ == '__main__':
    unittest.main()
