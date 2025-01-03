import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from operations import add, subtract, multiply, divide, exponentiation

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


    def test_divide_positive_numbers(self):
        self.assertEqual(divide(6, 2), 3)  

    def test_divide_negative_numbers(self):
        self.assertEqual(divide(-6, -2), 3)  

    def test_divide_mixed_numbers(self):
        self.assertEqual(divide(-6, 2), -3)  

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError) as context:
            divide(6, 0)
        self.assertEqual(str(context.exception), "Error: Division by 0!")

    def test_divide_by_one(self):
        self.assertEqual(divide(6, 1), 6)  

    def test_divide_large_numbers(self):
        self.assertEqual(divide(1000000000000, 1000000), 1000000)  

    def test_divide_decimal_numbers(self):
        self.assertEqual(divide(5.5, 2), 2.75)  

    def test_divide_small_result(self):
        self.assertEqual(divide(1, 2), 0.5) 


    def test_exponentiation_positive_numbers(self):
        self.assertEqual(exponentiation(2, 3), 8)  # 2^3 = 8

    def test_exponentiation_negative_numbers(self):
        self.assertEqual(exponentiation(-2, 3), -8)  # (-2)^3 = -8
        self.assertEqual(exponentiation(-2, 2), 4)   # (-2)^2 = 4

    def test_exponentiation_zero_exponent(self):
        self.assertEqual(exponentiation(5, 0), 1)    # 5^0 = 1
        self.assertEqual(exponentiation(0, 0), 1)    # 0^0 = 1 (mathematically undefined but commonly accepted as 1)

    def test_exponentiation_zero_base(self):
        self.assertEqual(exponentiation(0, 5), 0)    # 0^5 = 0
        with self.assertRaises(ValueError):
            exponentiation(0, -5)    # 0^-5 -> infinity (mathematically)

    def test_exponentiation_fractional_exponents(self):
        self.assertEqual(exponentiation(16, 0.5), 4)   # 16^(1/2) = sqrt(16) = 4
        self.assertEqual(exponentiation(27, 1/3), 3)   # 27^(1/3) = cube root of 27 = 3

    def test_exponentiation_large_numbers(self):
        self.assertEqual(exponentiation(10, 6), 1000000)  # 10^6 = 1,000,000

    def test_exponentiation_negative_fractional_exponent(self):
        self.assertAlmostEqual(exponentiation(8, -0.5), 0.35355339059327373, places=15)  # 8^(-1/2) = 1 / sqrt(8)

        