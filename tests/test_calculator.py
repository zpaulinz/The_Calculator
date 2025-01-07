import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from calculator import Calculator

class TestCalculatorMenu(unittest.TestCase):
    
    def setUp(self):
        """Set up a Calculator instance for testing."""
        self.calculator = Calculator()

    def test_add(self):
        """Test addition operation."""
        result = self.calculator.perform_operation('1', 3, 2)
        self.assertEqual(result, 5)

    def test_subtract(self):
        """Test subtraction operation."""
        result = self.calculator.perform_operation('2', 5, 3)
        self.assertEqual(result, 2)

    def test_multiply(self):
        """Test multiplication operation."""
        result = self.calculator.perform_operation('3', 4, 2)
        self.assertEqual(result, 8)

    def test_divide(self):
        """Test division operation."""
        result = self.calculator.perform_operation('4', 6, 2)
        self.assertEqual(result, 3)
    
    def test_divide_by_zero(self):
        """Test division by zero."""
        with self.assertRaises(ValueError):
            self.calculator.perform_operation('4', 5, 0)

    def test_exponentiation(self):
        """Test exponentiation operation."""
        result = self.calculator.perform_operation('5', 2, 3)
        self.assertEqual(result, 8)
    
    def test_exponentiation_zero_negative(self):
        """Test zero raised to negative exponent."""
        with self.assertRaises(ValueError):
            self.calculator.perform_operation('5', 0, -1)
            
if __name__ == '__main__':
    unittest.main()
