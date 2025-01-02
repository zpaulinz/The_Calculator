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

    @patch('builtins.input', side_effect=['0', '5'])  
    @patch('sys.stdout', new_callable=StringIO)
    def test_invalid_operation(self, mock_stdout, mock_input):
        main()
        output = mock_stdout.getvalue()
        self.assertIn("Error: Invalid choice. Please select a valid operation (1-5).", output)
        self.assertIn("Exit", output)

    @patch('builtins.input', side_effect=['4', '6', '0', '5']) 
    @patch('sys.stdout', new_callable=StringIO)
    def test_division_by_zero(self, mock_stdout, mock_input):
        main()
        output = mock_stdout.getvalue()
        self.assertIn("Error: Division by 0!", output)
        self.assertIn("Exit", output)

    @patch('builtins.input', side_effect=['1', '1000000000', '1000000000', '5'])  
    @patch('sys.stdout', new_callable=StringIO)
    def test_large_numbers(self, mock_stdout, mock_input):
        main()
        output = mock_stdout.getvalue()
        self.assertIn("The result is: 2000000000.0", output)
        self.assertIn("Exit", output)

    @patch('builtins.input', side_effect=['2', '-5', '-3', '5'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_subtraction_with_negatives(self, mock_stdout, mock_input):
        main()
        output = mock_stdout.getvalue()
        self.assertIn("The result is: -2.0", output)
        self.assertIn("Exit", output)

    @patch('builtins.input', side_effect=['4', '5', '3', '5'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_rounding_result(self, mock_stdout, mock_input):
        main()
        output = mock_stdout.getvalue()
        self.assertIn("The result is: 1.67", output)
        self.assertIn("Exit", output)

    @patch('builtins.input', side_effect=['1', '2', '3', '2', '3', '2', '5'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_complex_sequence(self, mock_stdout, mock_input):
        main()
        output = mock_stdout.getvalue()
        self.assertIn("The result is: 5.0", output)  # 2 + 3 = 5
        self.assertIn("The result is: 1.0", output)  # 3 - 2 = 1
        self.assertIn("Exit", output)

    @patch('builtins.input', side_effect=['1', 'abc', '5', '3', '5'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_invalid_number_input(self, mock_stdout, mock_input):
        main()
        output = mock_stdout.getvalue()
        self.assertIn("Error: Invalid input! Please enter a valid number.", output)
        self.assertIn("The result is: 8.0", output)  # 5 + 3 = 8
        self.assertIn("Exit", output)

    @patch('builtins.input', side_effect=['4', '1', '3', '5'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_division_small_result(self, mock_stdout, mock_input):
        main()
        output = mock_stdout.getvalue()
        self.assertIn("The result is: 0.33", output)  # 1 / 3 = 0.333... rounded
        self.assertIn("Exit", output)

if __name__ == '__main__':
    unittest.main()
