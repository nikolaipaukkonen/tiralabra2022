from turtle import st


def gcd(a, b):
    """Lasketaan suurin yhteinen nimittäjä Eukleideen funktiolla.
    Funktio palauttaa suurimman yhteisen nimittäjän. 

        Args:
            a, b: Verrattavat luvut.
    """
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    """kesken"""
    return a // gcd(a, b) * b


def calculate_d(e, ph):
    """Noudatellen https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm löytyvää pseudokoodia.
    
    Args:
        e: Avainten luontiin tarvittu alkuluku, joka on keskenään jaoton phi:n kanssa   
        l: Avainten luonnissa kahdesta suuresta alkuluvusta laskettu Carmichaelin funktion lambda"""
    g, x, y = extended_gcd(e, ph)
    if g != 1:
        raise Exception("Lukua ei ole")
    else:
        return x % ph

def invmod(e, m):
    g, x, y = extended_gcd(e, m)
    assert g == 1

    if x < 0:
        x += m
    return x

def extended_gcd(a, b):
    old_s, s = 1, 0
    old_t, t = 0, 1
    while b:
        q = a // b
        s, old_s = old_s - q * s, s
        t, old_t = old_t - q * t, t
        a, b = b, a % b
    return a, old_s, old_t

def string_to_int(message, max_code=0x110000):
    """Muuntaa viestin kokonaisluvuiksi, jotka voidaan salata.
    
        Args:
            message: Muunnettava merkkijono.
    """

    number = 0
    for e in [ord(c) for c in message]:
        number = (number * max_code) + e
    return number

def int_to_string(integer_message, max_code=0x110000):
    """Muuntaa kokonaislukumuotoisen viestin merkkijonoksi salauksen purun jälkeen.
    
        Args:
            integer_message: Kokonaislukumuotoinen viesti.
    """
    l = []
    while integer_message != 0:
        l.append(chr(integer_message % max_code))
        integer_message = integer_message // max_code
    return ''.join(reversed(l))

def exp_func(x, y):
    exp = bin(y)
    val = x
    counter_test = 0
    for i in range(3, len(exp)):
        print(counter_test)
        counter_test += 1
        val = val * val
        if (exp[i:i+1]=='1'):
            val = val*x
    return val