class Zwierze:
    def __init__(self, wiek, imie):
        self.wiek = wiek
        self.imie = imie

    def wydajDzwiek(self):
        print(f"{self.imie} wydaje dźwięk")

    def jedz(self):
        print(f"{self.imie} je")
