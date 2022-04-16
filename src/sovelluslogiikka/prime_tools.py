import random
from .math_tools import *
from datetime import datetime

class Avaingeneraattori:
    def __init__(self, size_in_bits):
        self.__size_in_bits = size_in_bits
        self.d = 0
        self.e = 65537
        self.n = 0
        self.p, self.q = 0,0
        self.ph = 0
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
        self.ph =(p-1)*(q-1)

        return self.ph

    def carmichael_lambda(self, p, q):
        """Laskee Carmichaelin funktiolla arvon purkuavainta varten.

        Args:
            p, q: Kaksi eri suuruista alkulukua
        """
        return p*q // gcd(p,q)

    def luo_p_ja_q(self):
        self.p, self.q = self.luo_alkuluku(), self.luo_alkuluku()

        while self.p == self.q:
            self.q = self.luo_alkuluku()
        
        return 

    def luo_avain(self):
        """Generoi avainparin. kesken. Tullaan eriyttämään erillisiksi
        osiksi.

        """
        start = datetime.now()
        print("Avaimen koko:", self.__size_in_bits)
        self.luo_p_ja_q()

        self.n = self.p * self.q
        self.phi_euler(self.p,self.q)

        while gcd(self.e, self.ph) != 1:
            self.luo_p_ja_q
            self.phi_euler(self.p, self.q)

        self.d = calculate_d(self.e, self.ph)
        self.dp = self.d%(self.p-1)
        self.dq = self.d%(self.q-1)
        self.qinv = invmod(self.q, self.p)

        #testailua, poistetaan lopullisesta versiosta
        print("p:", self.p)
        print("q:", self.q)
        print("e: ", self.e)
        print("n: ", self.n)
        print("phi:", self.ph)
        print("d: ", self.d)

        print("Avainten generointi kesti, ", datetime.now()-start, "sekuntia.")

        return 

    def salaa(self,message):
        """Salaa syötetyn viestin käyttäen avainparia.

        Args:
            message: Salattava viesti.
        """
        int_data = string_to_int(message)
        salattu = pow(int_data, self.e, self.n)
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

        int_data = pow(int(message_int), selpoetf.d, self.n)
        print("Viestin purkaminen kesti, ", datetime.now()-start, "sekuntia.")

        return int_to_string(int_data)

    def pura_nopea(self,message_int):
        """Purkaa syötetyn viestin avainparilla käyttäen chinese remainder theoremia.
        
        Args:
            message_int: Purettava viesti kokonaislukuna.
        """
        m1 = pow(message_int,self.dp, self.p)
        m2 = pow(message_int, self.dq, self.q)
        t = m1-m2
        if t < 0:
            t+= self.p
        h = (self.qinv * t) % self.p
        message = (m2+h*self.q) % self.n
        return message

    def vie(self):
        tiedostonimi = input("Anna kirjoitettavan avainparin tiedostonimi:")
        with open(tiedostonimi, 'w') as f:
            f.write(str(self.e))
            f.write("\n")
            f.write(str(self.d))
            f.write("\n")
            f.write(str(self.n))
            f.write("\n")

    def tuo(self):
        tiedostonimi = input("Anna luettavan avainparin tiedostonimi:")

        with open(tiedostonimi) as f:
            lines = f.readlines()
            self.e = lines[0]
            self.d = lines[1]
            self.n = lines[2]