"""
Stwórz klasy: `Kolo` i `Kwadrat`.
Klasy powinny przechowywać informację o figurze (promień lub bok).
Dodaj metody do obliczania pola i obwodu.
Pamiętaj, aby stworzyć odpowiedni konstruktor.
"""

from math import pi, pow

class Kolo:
    def __init__(self, promien):
        self.promien = promien

    def pole(self):
        return pi * pow(self.promien, 2)
    
    def obwod(self):
        obwod = 2 * pi * self.promien
        return obwod
    
    def wyswietl(self):
        print(f"To jest koło o promieniu {self.promien}, który ma pole {self.pole()} i obwód {self.obwod()}")

class Kwadrat:
    def __init__(self, bok):
        self.bok = bok
        # self.obwod = 4 * bok
    
    def obwod(self):
        return 4 * self.bok
    
    def pole(self):
        return pow(self.bok, 2)
    
    def wyswietl(self):
        print(f"To jest kwadrat o bok {self.bok}, który ma pole {self.pole()} i obwód {self.obwod()}")


# Testy
kolo1 = Kolo(10)
# print(kolo1.obwod())
# print(kolo1.pole())
kolo1.wyswietl()

kwadrat1 = Kwadrat(2)
kwadrat1.bok = 6

# print(kwadrat1.obwod)

# print(kwadrat1.obwod())
# print(kwadrat1.pole())

kwadrat1.wyswietl()