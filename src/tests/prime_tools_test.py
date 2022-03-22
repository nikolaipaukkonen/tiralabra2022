import unittest
from src.sovelluslogiikka.prime_tools import *

class TestPrime_tools(unittest.TestCase):
    def setUp(self):
        print("Test prime_tools")

    def test_generate_prime_palauttaa_oikean_pituisen_luvun(self):
        luku = generate_prime(1024)
        pituus_bitteina = luku.bit_length()
        self.assertEqual(1024, pituus_bitteina)