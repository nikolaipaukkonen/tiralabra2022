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

    def test_rabin_miller(self):
        testiluku = 102753878333786575683857826242754390887639315929469337484397294120531263673831701664588326518380603701910328930774259368694415405460819393604480081374772613977270118466703727722021192902358406600227638745550165159433408697229662195661488896949704887006228715501336694295416712143282609427849565833913043261090
        self.assertEqual(True, self.prime_prime_tools.rabin_miller(testiluku))

    def test_phi_euler_palauttaaOikein(self):
        self.assertEqual(self.prime_prime_tools.phi_euler(7, 13), 72)

    """def test_salaa(self):
        message = "testi"
        self.prime_prime_tools.p = 240895643531179921752890446157156649727
        self.prime_prime_tools.q = 255082517078591894838835283908870330723
        self.n = 61448267105200587504126390670239288107063610131941075367121906411697157662621
        self.prime_ph = 61448267105200587504126390670239288106567631971331303550530180681631130682172
        self.prime_public_exponent = 65537
        self.prime_private_exponent = 29227236251328451312672655903881762803575479863441100359752915028271138526705
        self.assertEqual(203509088203007837383303304874265624241791472077172500676634463466765026685, self.prime_prime_tools.salaa(message))

    def test_pura(self):
        message = 203509088203007837383303304874265624241791472077172500676634463466765026685
        self.prime_prime_tools.p = 240895643531179921752890446157156649727
        self.prime_prime_tools.q = 255082517078591894838835283908870330723
        self.n = 61448267105200587504126390670239288107063610131941075367121906411697157662621
        self.prime_ph = 36612
        self.prime_public_exponent = 65537
        self.prime_private_exponent = 29227236251328451312672655903881762803575479863441100359752915028271138526705
        self.assertEqual("testi", self.prime_prime_tools.pura(message))"""
    