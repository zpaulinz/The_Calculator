import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from operations import add, subtract, multiply

class TestOperations(unittest.TestCase):  
    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)  

    def test_add_negative_numbers(self):
        self.assertEqual(add(-2, -3), -5)  

    def test_add_mixed_numbers(self):
        self.assertEqual(add(-2, 3), 1)  

    def test_add_zero(self):
        self.assertEqual(add(0, 0), 0)  
        self.assertEqual(add(2, 0), 2)  


    def test_subtract_positive_numbers(self):
        self.assertEqual(subtract(5, 3), 2)

    def test_subtract_negative_numbers(self):
        self.assertEqual(subtract(-5, -3), -2)

    def test_subtract_mixed_numbers(self):
        self.assertEqual(subtract(-5, 3), -8)

    def test_subtract_zero(self):
        self.assertEqual(subtract(0, 0), 0)
        self.assertEqual(subtract(5, 0), 5)
        self.assertEqual(subtract(0, 5), -5)


    def test_multiply_positive_numbers(self):
        self.assertEqual(multiply(3, 4), 12)

    def test_multiply_negative_numbers(self):
        self.assertEqual(multiply(-3, -4), 12)

    def test_multiply_mixed_numbers(self):
        self.assertEqual(multiply(-3, 4), -12)

    def test_multiply_by_zero(self):
        self.assertEqual(multiply(0, 5), 0)
        self.assertEqual(multiply(5, 0), 0)

    def test_multiply_by_one(self):
        self.assertEqual(multiply(1, 7), 7)
        self.assertEqual(multiply(7, 1), 7)

    def test_multiply_large_numbers(self):
        self.assertEqual(multiply(1000000, 1000000), 1000000000000)
