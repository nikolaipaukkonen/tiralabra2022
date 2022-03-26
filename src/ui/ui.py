#from sovelluslogiikka.math_tools import Math_tools
from sovelluslogiikka.prime_tools import Prime_tools

class UI:
    def __init__(self):
        syote = int(input("Syötä salausavaimen pituus bitteinä (oletus 1024):"))
        self.key_len = syote if syote >= 1024 else 1024
        self.__prime_tools = Prime_tools(1024)

    def start(self):
        """Aloittaa käyttöliittymän
        
        """
        self.ohje() 

    def ohje(self):
        """Tulostaa vaihtoehdot ja kysyy syötteen.
        
        """
        print("[1] Luo uusi avain\n[2] Vie avain\n[3] Tuo avain \n[4] Salaa viesti \n[5] Pura viesti")
        valinta = input(":::")
        self.toiminto(valinta)

    def toiminto(self, valinta):
        """Toiminnon valinta.
        
        Args:
            valinta: Valittu toiminto.
        """
        if (valinta == "1"):
            self.luo_avain()
        elif (valinta == "2"):
            self.vie()
        elif (valinta == "3"):
            self.tuo()

    def tuo(self):
        #tbd   
        return 0

    def vie(self):
        #tbd
        return 0

    def luo_avain(self):
        """Generoi avainparin. wip: nyt luo vain p, q ja n."""
        print(self.key_len)
        p = self.__prime_tools.generate_prime()
        q = self.__prime_tools.generate_prime()

        while(p == q):
            q = self.__prime_tools.generate_prime()

        n = p * q
        print("p:", p)
        print("q:", q)
        print("Julkisen avaimen ensimmäinen osa: ", n)