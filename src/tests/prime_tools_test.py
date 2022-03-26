import unittest
from src.sovelluslogiikka.prime_tools import Prime_tools

class TestPrime_tools(unittest.TestCase):
    def setUp(self):
        print("Test prime_tools")
        self.prime_tools = Prime_tools(1024)

    def test_generate_prime_palauttaa_oikean_pituisen_luvun(self):
        luku = self.prime_tools.generate_prime()
        pituus_bitteina = luku.bit_length()
        self.assertEqual(1024, pituus_bitteina)

    def test_sieve_of_erastothenes(self):
        luvut = self.prime_tools.sieve_of_erastothenes(200)
        vertailu_alkuluvut = [2, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99, 101, 103, 105, 107, 109, 111, 113, 115, 117, 119, 121, 123, 125, 127, 129, 131, 133, 135, 137, 139, 141, 143, 145, 147, 149, 151, 153, 155, 157, 159, 161, 163, 165, 167, 169, 171, 173, 175, 177, 179, 181, 183, 185, 187, 189, 191, 193, 195, 197, 199]
        self.assertEqual(luvut, vertailu_alkuluvut)

    def test_rabin_miller(self):
        testiluku = 102753878333786575683857826242754390887639315929469337484397294120531263673831701664588326518380603701910328930774259368694415405460819393604480081374772613977270118466703727722021192902358406600227638745550165159433408697229662195661488896949704887006228715501336694295416712143282609427849565833913043261090
        self.assertEqual(True, self.prime_tools.rabin_miller(testiluku))