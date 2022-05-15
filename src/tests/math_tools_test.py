import unittest
from src.sovelluslogiikka.math_tools import *

class TestMath_tools(unittest.TestCase):
    def setUp(self):
        "Test math_tools.py"

    def test_gcd_with_two_primes(self):
        self.assertEqual(gcd(163, 227), 1)

    def test_lcm(self):
        self.assertEqual(lcm(163, 227), 37001)

    def test_calculate_d_oikein(self):
        self.assertEqual(calculate_d(65537, 36612), 1205)

    def test_calculate_d_virheellinen(self):
        with self.assertRaises(Exception):
            calculate_d(10,15)

    def test_invmod(self):
        self.assertEqual(invmod(3,7), 5)

    def test_extended_gcd(self):
        self.assertEqual(extended_gcd(65537, 36612), (1, 1205, -2157))

    def test_string_to_int(self):
        testiviesti = string_to_int("testi")
        self.assertEqual(testiviesti, 178720239038199635312377961)

    def test_int_to_string(self):
        testiviesti = 178720239038199635312377961
        self.assertEqual(int_to_string(testiviesti), "testi")
