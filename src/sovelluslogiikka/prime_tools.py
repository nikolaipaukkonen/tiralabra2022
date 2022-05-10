import random
from .math_tools import *
import os.path
from datetime import datetime

class Avaingeneraattori:
    def __init__(self, size_in_bits):
        self.__size_in_bits = size_in_bits
        self.private_exponent = 0
        self.public_exponent = 65537
        self.modulus_n = 0
        self.prime_p, self.prime_q = 0,0
        self.carmichaelin_luku = 0
        self.small_primes = self.sieve_of_erastothenes(1500)

    def random_seed(self, size_in_bits):
        """Luo pseudosatunnaisen siemenluvun jolla alkuluku generoidaan

        Args:
            size_in_bits: Luvun koko bitteinä.
        """
        return (random.randrange(2**(size_in_bits-1)+1, 2**size_in_bits-1))

    def sieve_of_erastothenes(self,amount):
        """Erastotheneen seula pienten alkulukujen luontiin

        Args:
            amount: Kuinka monta alkulukua luodaan.
        """
        primes = []

        prime = [True for i in range(amount+1)]
        p = 2
        while p * p <= amount:
            if prime[p] is True:
                for i in range(p**2, amount+1,p):
                    prime[i] = False
            p += 1
        prime[0] = False
        prime[1] = False

        for p in range(amount+1):
            if prime[p]:
                primes.append(p)

        return primes

    def easy_possible_prime(self,size_in_bits):
        """Helppo mahdollisen alkuluvun luonti ja tarkistus jakamalla Erastotheneen
        seulalla saaduilla pienillä alkuluvuilla.

        Args:
            size_in_bits: luvun koko bitteinä.
        """
        while True:
            possible_prime = self.random_seed(size_in_bits)

            for factor in self.small_primes:
                if possible_prime % factor == 0 and factor**2 <= possible_prime:
                    break
                else: return possible_prime

    def rabin_miller(self,possible_prime):
        """Rabin-Millerin testi mahdolliselle alkuluvulle

        Args:
            possible_prime: Testattava luku
        """
        maxDivisions = 0
        evenPossible = possible_prime - 1

        while evenPossible % 2 == 0:
            evenPossible >>= 1
            maxDivisions += 1
        assert(2**maxDivisions * evenPossible == possible_prime - 1)

        def testPart(testable):
            if pow(testable, evenPossible, possible_prime) == 1:
                return False

            for i in range(maxDivisions):
                if pow(testable, 2**i * evenPossible, possible_prime) == possible_prime - 1:
                    return False
                return True

        amountOfTests = 10 # kasvata todennäköisyyttä
        for _ in range(amountOfTests):
            testable = random.randrange(2, possible_prime)
            if testPart(testable):
                return False
        return True

    def luo_alkuluku(self):
        """Alkulukugeneraattori, joka kutsuu muita luokan metodeja

        Args:
            size_in_bits: generoitavan alkuluvun koko.
        """
        while True:
            possible_prime = self.easy_possible_prime(self.__size_in_bits)
            if not self.rabin_miller(possible_prime):
                continue
            else:
                return possible_prime

    def phi_euler(self,p, q):
        """Laskee Eulerin phi-funktiolla keskenään jaottomien lukujen määrän purkuavaimen
        määrittelyä varten.
        
        Args:
            p, q: Kaksi eri suuruista alkulukua
        """
        self.carmichaelin_luku =(p-1)*(q-1)

        return self.carmichaelin_luku

    def carmichael_lambda(self, p, q):
        """Laskee Carmichaelin funktiolla arvon purkuavainta varten.

        Args:
            p, q: Kaksi eri suuruista alkulukua
        """
        return p*q // gcd(p,q)

    def luo_p_ja_q(self):
        self.prime_p, self.prime_q = self.luo_alkuluku(), self.luo_alkuluku()

        while self.prime_p == self.prime_q:
            self.prime_q = self.luo_alkuluku()
        
        return 

    def luo_avain(self):
        """Generoi avainparin. kesken. Tullaan eriyttämään erillisiksi
        osiksi.

        """
        start = datetime.now()
        print("Avaimen koko:", self.__size_in_bits)
        self.luo_p_ja_q()

        self.modulus_n = self.prime_p * self.prime_q
        self.phi_euler(self.prime_p,self.prime_q)

        while gcd(self.public_exponent, self.carmichaelin_luku) != 1:
            self.luo_p_ja_q
            self.phi_euler(self.prime_p, self.prime_q)

        self.private_exponent = calculate_d(self.public_exponent, self.carmichaelin_luku)
        self.private_exponentp = self.private_exponent%(self.prime_p-1)
        self.private_exponentq = self.private_exponent%(self.prime_q-1)
        self.prime_qinv = invmod(self.prime_q, self.prime_p)

        #testailua, poistetaan lopullisesta versiosta
        print("p:", self.prime_p)
        print("q:", self.prime_q)
        print("e: ", self.public_exponent)
        print("n: ", self.modulus_n)
        print("phi:", self.carmichaelin_luku)
        print("d: ", self.private_exponent)

        print("Avainten generointi kesti: ", datetime.now()-start, "sekuntia.")

        return 

    def salaa(self,message):
        """Salaa syötetyn viestin käyttäen avainparia.

        Args:
            message: Salattava viesti.
        """
        int_data = string_to_int(message)
        salattu = pow(int_data, self.public_exponent, self.modulus_n)
        self.vika_viesti = salattu
        return salattu

    def pura(self,message_int):
        """Purkaa syötetyn viestin käyttäen avainparia.

        Args:
            message_int: Purettava viesti.
        """

        start = datetime.now()
        if message_int == "":
            message_int = int(self.vika_viesti)

        int_data = pow(int(message_int), self.private_exponent, self.modulus_n)
        print("Viestin purkaminen kesti: ", datetime.now()-start, "sekuntia.")

        return int_to_string(int_data)

    def pura_nopea(self,message_int):
        """Purkaa syötetyn viestin avainparilla käyttäen chinese remainder theoremia.
        
        Args:
            message_int: Purettava viesti kokonaislukuna.
        """
        m1 = pow(message_int,self.private_exponentp, self.prime_p)
        m2 = pow(message_int, self.private_exponentq, self.prime_q)
        t = m1-m2
        if t < 0:
            t+= self.prime_p
        h = (self.prime_qinv * t) % self.prime_p
        message = (m2+h*self.prime_q) % self.modulus_n
        return message

    def vie(self):
        """Vie luodun avaimen erilliseen tekstitiedostoon.
        
        """
        tiedostonimi = input("Anna kirjoitettavan avainparin tiedostonimi:")
        with open(tiedostonimi, 'w') as f:
            f.write(str(self.public_exponent))
            f.write("\n")
            f.write(str(self.private_exponent))
            f.write("\n")
            f.write(str(self.modulus_n))
            f.write("\n")

    def tuo(self):
        """Tuo aiemmin luodun avaimen ohjelmaan.
        
        """
        tiedostonimi = input("Anna luettavan avainparin tiedostonimi:")
        if os.path.exists(tiedostonimi):
            with open(tiedostonimi) as f:
                lines = f.readlines()
                self.public_exponent = int(lines[0])
                self.private_exponent = int(lines[1])
                self.modulus_n = int(lines[2])
            print(tiedostonimi, "tuotu.")
            return True

        else: 
            print("Tiedostoa ei löydy.")
            return False