import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from operations import add

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