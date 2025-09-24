from random import randint, choice
# from typing import Self

class Postac:
    def __init__(self):
        self.nazwa = ""
        self.zycie = 1
        self.max_zycie = 1

    def atakuj(self, przeciwnik: 'Postac'):
        atak = randint(0, 3)

        if atak == 0:
            print(f"{przeciwnik.nazwa} unika ataku {self.nazwa}.")
        else:
           print(f"{self.nazwa} atakuje {przeciwnik.nazwa}, zadając {atak} obrażeń.")
           przeciwnik.zycie -= atak

class Przeciwnik(Postac):
    def __init__(self):
        super().__init__()
        self.nazwa = choice(['goblin', 'szkielet', 'zombie', 'wilk'])
        self.zycie = randint(1, 10)

class Gracz(Postac):
    def __init__(self, nazwa):
        super().__init__()
        self.zycie = 10
        self.max_zycie = 10
        self.nazwa = nazwa
    
    def odpoczynek(self):
        self.zycie += 1
        if self.zycie > self.max_zycie:
            self.zycie = self.max_zycie
        print(f"{self.nazwa} odpoczywa. Życie: {self.zycie}/{self.max_zycie}")


    def walka(self, przeciwnik: Przeciwnik):
        walka = True
        while walka:
            print(f"Życie gracza: {self.zycie}")
            print(f"Życie {przeciwnik.nazwa}: {przeciwnik.zycie}")
            akcja = input('Akcja (atak, uciekaj): ')

            match akcja:
                case "atak":
                    self.atakuj(przeciwnik)
                    if przeciwnik.zycie <= 0:
                        print(f"{self.nazwa} zabija {przeciwnik.nazwa}")
                        return True
                    przeciwnik.atakuj(self)
                case "uciekaj":
                    print(f"{self.nazwa} ucieka")
                    przeciwnik.atakuj(self)
                    walka = False
                case _:
                    print("Nieznana akcja")

            if self.zycie <= 0:
                print(f"{self.nazwa} ginie")
                return False
        
        return True

# Przygotowanie gry
nazwa_gracza = input("Podaj nazwę swojej postaci: ")
gracz = Gracz(nazwa_gracza)

# Główna pętla gry
gra = True
while gra:
    akcja = input("Akcja (zwiedzaj, odpocznij): ")
    match akcja:
        case "zwiedzaj":
            rzut_koscia = randint(1, 20)
            if rzut_koscia <= 5:
                print(f"{gracz.nazwa} znalazł jaskinie.")
            else:
                przeciwnik = Przeciwnik()
                print(f"{gracz.nazwa} natrafił na {przeciwnik.nazwa}")
                gra = gracz.walka(przeciwnik)
        case "odpocznij":
            gracz.odpoczynek()
        case _:
            print("Nieznana akcja.")