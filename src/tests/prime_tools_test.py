import unittest
from src.sovelluslogiikka.prime_tools import Avaingeneraattori

class TestAvaingeneraattori(unittest.TestCase):
    def setUp(self):
        print("Test prime_tools")
        self.prime_prime_tools = Avaingeneraattori(1024)

    def test_luo_alkuku_palauttaa_oikean_pituisen_luvun(self):
        luku = self.prime_prime_tools.luo_alkuluku()
        pituus_bitteina = luku.bit_length()
        self.assertEqual(1024, pituus_bitteina)

    def test_sieve_of_erastothenes(self):
        luvut = self.prime_prime_tools.sieve_of_erastothenes(200)
        vertailu_alkuluvut = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]
        self.assertEqual(luvut, vertailu_alkuluvut)

    def test_luo_avain_muuttaa_muuttujia(self):
        self.prime_prime_tools.luo_avain()
        self.assertIsNot(self.prime_prime_tools.private_exponent, 0)

    def test_carmichael_lambda(self):
        l = self.prime_prime_tools.carmichael_lambda(3, 7)
        self.assertEqual(21, l)

    def test_rabin_miller(self):
        testiluku = 102753878333786575683857826242754390887639315929469337484397294120531263673831701664588326518380603701910328930774259368694415405460819393604480081374772613977270118466703727722021192902358406600227638745550165159433408697229662195661488896949704887006228715501336694295416712143282609427849565833913043261090
        self.assertEqual(True, self.prime_prime_tools.rabin_miller(testiluku))

    def test_phi_euler_palauttaaOikein(self):
        self.assertEqual(self.prime_prime_tools.phi_euler(7, 13), 72)

