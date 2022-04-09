from turtle import st


def gcd(a, b):
    """Lasketaan suurin yhteinen nimittäjä Eukleideen laajennetulla funktiolla.
    Funktio palauttaa suurimman yhteisen nimittäjän. 

        Args:
            a, b: Verrattavat luvut.
    """
    temp = 0

    while (b != 0):
        temp = a
        a = b
        b = temp % b

    return a

def calculate_d(e, ph):
    """Noudatellen https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm löytyvää pseudokoodia.
    
    Args:
        e: Avainten luontiin tarvittu alkuluku, joka on keskenään jaoton phi:n kanssa   
        ph: Avainten luonnissa kahdesta suuresta alkuluvusta laskettu phi"""
    old_r = e
    r = ph
    old_s = 1 
    s = 0

    while r != 0:
        quotidient = old_r // r
        old_r, r = r, (old_r - (quotidient * r))
        old_s, s = s, (old_s - (quotidient * s))

    return abs(old_s)

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

def divide_into_blocks(message):
    inp = message
    output = []
    while True:
        if len(inp) < 30:
            output.append(inp)
            break
        output.append(inp[:30])
        inp = inp[30:]
        if len(inp) == 0:
            break
    return output