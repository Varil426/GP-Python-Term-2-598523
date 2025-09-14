"""
Stwórz nową klasę bazową `Figura`, która będzie miała metody `pole`, `obwod` i `wyswietl`.
Klasy `Kolo` i `Kwadrat` powinny dziedziczyć po klasie `Figura` i implementować te metody.

Dodatkowo, stwórz klasę `Prostokat`, która również dziedziczy po `Figura` i implementuje odpowiednie metody.
Czy klasa `Kwadrat` może dziedziczyć po `Prostokat`? Dlaczego tak lub dlaczego nie?
"""

from math import pi, pow

# Klasy


class Kolo:
    def __init__(self, promien):
        self.promien = promien

    def pole(self):
        return pi * pow(self.promien, 2)

    def obwod(self):
        obwod = 2 * pi * self.promien
        return obwod

    def wyswietl(self):
        print(
            f"To jest koło o promieniu {self.promien}, który ma pole {self.pole()} i obwód {self.obwod()}"
        )


class Kwadrat:
    def __init__(self, bok):
        self.bok = bok

    def obwod(self):
        return 4 * self.bok

    def pole(self):
        return pow(self.bok, 2)

    def wyswietl(self):
        print(
            f"To jest kwadrat o bok {self.bok}, który ma pole {self.pole()} i obwód {self.obwod()}"
        )


# Testy
