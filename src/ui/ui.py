from sovelluslogiikka.prime_tools import Avaingeneraattori
import sys

class UI:
    def __init__(self):
        syote = input("Syötä salausavaimen pituus bitteinä (oletus 1024):")
        self.key_len = int(syote) if syote != "" else 1024
        self.__prime_tools = Avaingeneraattori(self.key_len)
        self.avain_on = 0

    def start(self):
        """Aloittaa käyttöliittymän
        
        """
        self.ohje() 

    def ohje(self):
        """Tulostaa vaihtoehdot ja kysyy syötteen.
        
        """
        while(True):
            print("[1] Luo uusi avain\n[2] Vie avain\n[3] Tuo avain \n[4] Salaa viesti \n[5] Pura viesti \n[6] Poistu")
            valinta = input("::: ")
            self.toiminto(valinta)

    def toiminto(self, valinta):
        """Toiminnon valinta.
        
        Args:
            valinta: Valittu toiminto.
        """
        if (valinta == "1"):
            self.__prime_tools.luo_avain()
            self.avain_on = 1
        elif (valinta == "2"):
            self.vie()
        elif (valinta == "3"):
            self.tuo()
        elif (valinta == "4"):
            if (self.avain_on):
                salattava = input("Syötä salattava viesti:")
                salattu = self.__prime_tools.salaa(salattava)
                print("Viesti salattuna:", salattu)
            else:
                print("Ei salausavainta!")
        elif (valinta == "5"):
            if (self.avain_on):
                purettava = input("Syötä purettava viesti (tyhjä = pura viimeksi salattu):")
                print("Purettu viesti:", self.__prime_tools.pura(purettava))
            else:
                print("Ei purkuavainta!")
        elif (valinta == "6"):
            sys.exit(0)


    def tuo(self):
        #tbd  
        print("Ei vielä toteutettu") 
        return 0

    def vie(self):
        #tbd
        print("Ei vielä toteutettu") 
        return 0
