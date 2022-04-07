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

def string_to_int(message):
    """Muuntaa viestin kokonaisluvuiksi, jotka voidaan salata.
    
        Args:
            message: Muunnettava merkkijono.
    """

    if message == "":
        return string_to_int(" ")

    return int('1' + "".join(list(map((lambda x: str(ord(x)).zfill(3)), message))))

def int_to_string(integer_message):
    """Muuntaa kokonaislukumuotoisen viestin merkkijonoksi salauksen purun jälkeen.
    
        Args:
            integer_message: Kokonaislukumuotoinen viesti.
    """
    i = str(integer_message)[1: ]

    list_of_numbers = [i[3*n:3*(n+1)] for n in range(0, int(len(i)/3))]
    return "".join(list(map((lambda x: chr(int(x))), list_of_numbers)))