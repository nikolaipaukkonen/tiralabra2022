import random
from sovelluslogiikka.math_tools import gcd

class Prime_tools:
    def __init__(self, size_in_bits):
        self.__size_in_bits = size_in_bits

    def random_seed(self, size_in_bits):
        """Luo siemenluvun jolla alkuluku generoidaan

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
                for i in range(p*p, amount+1,p):
                    prime[i] = False
                p += 1

            for p in range(2, amount+1):
                if prime[p]:
                    primes.append(p)

        return primes

    def easy_possible_prime(self,size_in_bits):
        """Helppo mahdollisen alkuluvun luonti ja tarkistus

        Args:
            size_in_bits: luvun koko bitteinä.
        """
        easy_primes = self.sieve_of_erastothenes(1500)

        while True:
            possible_prime = self.random_seed(size_in_bits)

            for factor in easy_primes:
                if possible_prime % factor == 0 and factor**2 <= possible_prime:
                    break
            return possible_prime

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

    def luo_avain(self):
        """Generoi avainparin. kesken. Tullaan eriyttämään erillisiksi
        osiksi.

        """
        print(self.__size_in_bits)
        p = self.generate_prime()
        q = self.generate_prime()

        while p == q:
            q = self.generate_prime()

        n = p * q
        ph = self.phi(p,q)
        e = 65537

        while gcd(e, ph) != 1:
            p, q = self.generate_prime(), self.generate_prime()
            ph = self.phi(p, q)

        d = 0

        P = (e, n)
        S = (d, n)

        print("p:", p)
        print("q:", q)
        print("Julkisen avaimen ensimmäinen osa: ", n)
        print("phi:", ph)
        print("S:", S)
        print("P:", P)

    def salaa(self,viesti):
        """Salaa syötetyn viestin käyttäen avainparia. Kesken.

        Args:
            viesti: Salattava viesti.
        """
        return viesti

    def pura(self,viesti):
        """Purkaa syötetyn viestin käyttäen avainparia. Kesken.

        Args:
            viesti: Purettava viesti.
        """
        return viesti
