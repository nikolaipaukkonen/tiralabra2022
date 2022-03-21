import random

def random_seed(size_in_bits):
    return (random.randrange(2**(size_in_bits-1)+1, 2**size_in_bits-1))

def sieve_of_erastothenes(amount):
    primes = []

    prime = [True for i in range(amount+1)]
    p = 2
    while (p * p <= amount):
        if (prime[p] == True):
            for i in range(p*p, amount+1,p):
                prime[i] = False
            p += 1

        for p in range(2, amount+1):
            if prime[p]:
                primes.append(p)

    return primes

def easy_possible_prime(size_in_bits):
    easy_primes = sieve_of_erastothenes(1500)

    while True:
        possible_prime = random_seed(size_in_bits)

        for factor in easy_primes:
            if possible_prime % factor == 0 and factor**2 <= possible_prime:
                break
            else: 
                return possible_prime

def rabin_miller(possible_prime):
    # riittääkö että on todennäköisesti alkuluku?
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

def generate_prime(size_in_bits):
    while True:
        possible_prime = easy_possible_prime(size_in_bits)
        if not rabin_miller(possible_prime):
            continue
        else:
            return possible_prime