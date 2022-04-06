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
    old_r = e
    r = ph
    old_s = 1 
    s = 0

    while r != 0:
        quotidient = old_r // r
        old_r, r = r, (old_r - (quotidient * r))
        old_s, s = s, (old_s - (quotidient * s))

    return abs(old_s)
