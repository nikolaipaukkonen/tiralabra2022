import random
from telnetlib import ENCRYPT
from sovelluslogiikka.math_tools import gcd, calculate_d, divide_into_blocks, int_to_string, string_to_int

class Avaingeneraattori:
    def __init__(self, size_in_bits):
        self.__size_in_bits = size_in_bits
        self.d = 0
        self.e = 0
        self.n = 0
        self.p, self.q = 0,0
        self.small_primes = self.sieve_of_erastothenes(1500)
        self.dp, self.dq, self.qinv = 0,0,0

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
        for i in range(amountOfTests):
            testable = random.randrange(2, possible_prime)
            if testPart(testable):
                return False
        return True

    def generate_prime(self):
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

    def phi(self,p, q):
        return ((p-1)*(q-1))

    def luo_p_ja_q(self):
        self.p, self.q = self.generate_prime(), self.generate_prime()

        while self.p == self.q:
            self.q = self.generate_prime() # korjaa omaksi paketikseen
        
        return 

    def luo_avain(self):
        """Generoi avainparin. kesken. Tullaan eriyttämään erillisiksi
        osiksi.

        """
        print("Avaimen koko:", self.__size_in_bits)
        self.luo_p_ja_q()

        self.n = self.p * self.q
        ph = self.phi(self.p,self.q)
        self.e = 65537

        while gcd(self.e, ph) != 1:
            self.luo_p_ja_q
            ph = self.phi(self.p, self.q)

        self.d = calculate_d(self.e, ph)
        # apuluvut chinese remainder algorithmiin
        self.dp = self.d % (self.p-1)
        self.dq = self.d % (self.q-1)
        self.qinv = self.q**-1 % self.p

        #testailua
        print("p:", self.p)
        print("q:", self.q)
        print("e: ", self.e)
        print("n: ", self.n)
        print("phi:", ph)
        print("d: ", self.d)

        return 1

    def salaa(self,message):
        """Salaa syötetyn viestin käyttäen avainparia.

        Args:
            message: Salattava viesti.
        """
        encrypted_message = int(message)**self.e % self.n
        return encrypted_message

    def pura(self,message_int):
        """Purkaa syötetyn viestin käyttäen avainparia.

        Args:
            message_int: Purettava viesti.
        """
        m1 = int(message_int)**self.dp % self.p
        m2 = int(message_int)**self.dq % self.q
        h = self.qinv(m1-m2) % self.p
        message = m2 + h*self.q % (self.n)
        return message
