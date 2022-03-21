import sovelluslogiikka.math_tools
import sovelluslogiikka.prime_tools

class UI:
    def __init__(self):
        self.__ui = 0

    def start(self):
        syote = int(input("Syötä salausavaimen pituus bitteinä (oletus 1024):"))
        key_len = syote if syote >= 1024 else 1024
        self.generate_key(key_len)

    def generate_key(self,key_len):
        print(key_len)
        #generate_p_and_q(key_len)