import unittest
from src.sovelluslogiikka.math_tools import *

class TestMath_tools(unittest.TestCase):
    def setUp(self):
        "Test math_tools.py"

    def test_gcd_with_two_primes(self):
        self.assertEqual(gcd(163, 227), 1)

    def test_lcm(self):
        self.assertEqual(lcm(163, 227), 37001)

    def test_calculate_d(self):
        self.assertEqual(calculate_d(65537, 36612), 1205)

    def test_extended_gcd(self):
        self.assertEqual(extended_gcd(65537, 36612), (1, 1205, -2157))

    def test_string_to_int(self):
        self.assertEqual("tbd", "tbd")

    def test_int_to_string(self):
        self.assertEqual("tbd", "tbd")
