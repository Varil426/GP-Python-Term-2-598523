class Zwierze:
    def __init__(self, wiek, imie):
        self.wiek = wiek
        self.imie = imie

    def wydajDzwiek(self):
        print(f"{self.imie} wydaje dźwięk")

    def jedz(self):
        print(f"{self.imie} je")

class Pies(Zwierze):
    def __init__(self, wiek, imie):
        super().__init__(wiek, imie)
        self.rasa = "Mops"
    
    def wypiszRase(self):
        print(f"{self.imie} jest rasy: {self.rasa}")

    def wydajDzwiek(self):
        super().wydajDzwiek()
        print("Hau!")

class Kot(Zwierze):
    def __init__(self, wiek, imie, rasa):
        super().__init__(wiek, imie)
        self.rasa = rasa

    def wypiszRase(self):
        print(f"{self.imie} jest rasy: {self.rasa}")

    def wydajDzwiek(self):
        super().wydajDzwiek()
        print("Miau!")

zwierz1 = Pies(8, "Azor")
zwierz1.wydajDzwiek()
zwierz1.jedz()
zwierz1.wypiszRase()

zwierz2 = Pies(3, "Kajtek")
zwierz2.wydajDzwiek()
zwierz2.jedz()
zwierz2.wypiszRase()

zwierz3 = Kot(4, "Ramzes", "Pers")
zwierz3.wydajDzwiek()
zwierz3.jedz()
zwierz3.wypiszRase()

zwierz4 = Kot(4, "Ramzes 2", "Sfinks")
zwierz4.wydajDzwiek()
zwierz4.jedz()
zwierz4.wypiszRase()

# TODO Stwórz klasę `Ptak` z metodą `lec()` i klasę `Orzel` z metodą `poluj()`. W metodzie `poluj()` wywołaj `lec()`.

class Ptak(Zwierze):
    def __init__(self, wiek, imie):
        super().__init__(wiek, imie)

    def lec(self):
        print(f"Ptak {self.imie} leci!")

class Orzel(Ptak):
    def __init__(self, wiek, imie):
        super().__init__(wiek, imie)

    def poluj(self):
        self.lec()
        print(f"{self.imie} poluje!")

orzel1 = Orzel(1, "Ares")
orzel1.poluj()