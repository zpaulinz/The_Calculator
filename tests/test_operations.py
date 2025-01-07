import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from operations import add, subtract, multiply, divide, exponentiation

class TestOperations(unittest.TestCase):  
    
    def test_add(self):
        self.assertEqual(add(3, 2), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(3, 5), -2)
        self.assertEqual(subtract(0, 0), 0)

    def test_multiply(self):
        self.assertEqual(multiply(3, 2), 6)
        self.assertEqual(multiply(-1, 3), -3)
        self.assertEqual(multiply(0, 5), 0)

    def test_divide(self):
        self.assertEqual(divide(6, 2), 3)
        self.assertEqual(divide(-6, 2), -3)
        self.assertEqual(divide(5, 2), 2.5)

        # Test division by zero
        with self.assertRaises(ValueError):
            divide(1, 0)

    def test_exponentiation(self):
        self.assertEqual(exponentiation(2, 3), 8)
        self.assertEqual(exponentiation(2, -3), 0.125)
        self.assertEqual(exponentiation(0, 3), 0)

        # Test invalid exponentiation (0 raised to a negative power)
        with self.assertRaises(ValueError):
            exponentiation(0, -1)
            
if __name__ == '__main__':
    unittest.main()            