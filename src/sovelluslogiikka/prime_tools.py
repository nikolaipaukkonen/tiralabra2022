import random
from sovelluslogiikka.math_tools import gcd, calculate_d, int_to_string, string_to_int

class Avaingeneraattori:
    def __init__(self, size_in_bits):
        self.__size_in_bits = size_in_bits
        self.d = 0
        self.e = 0
        self.n = 0
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
        print("Avaimen koko:", self.__size_in_bits)
        p, q = self.generate_prime(), self.generate_prime()

        while p == q:
            q = self.generate_prime()

        self.n = p * q
        ph = self.phi(p,q)
        self.e = 65537

        while gcd(self.e, ph) != 1:
            p, q = self.generate_prime(), self.generate_prime()
            ph = self.phi(p, q)

        self.d = calculate_d(self.e, ph)

        #testailua
        print("p:", p)
        print("q:", q)
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
        self.msg_size = len(message.encode())
        int_message = int.from_bytes(message.encode(), "big")
        encrypted_message = pow(int_message, self.e, self.n)

        return encrypted_message

    def pura(self,message_int):
        """Purkaa syötetyn viestin käyttäen avainparia.

        Args:
            message_int: Purettava viesti.
        """
        decrypted_int = pow(int(message_int), self.d, self.n)
        message = int_to_string(decrypted_int)

        return message
