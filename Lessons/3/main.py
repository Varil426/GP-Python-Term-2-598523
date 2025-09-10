class Samochod:
    marka = ""
    model = ""
    typSilnika = ""
    mocKM = 0
    LicznikSamochodow = 0

    def wyswietl(self):
        print(self.marka)
        print(self.model)
        print(self.typSilnika, self.mocKM)

    def __init__(self, marka, model, typSilnika, mocKM):
        print("Utworzenie obiektu klasy Samochod")
        self.marka = marka
        self.model = model
        self.typSilnika = typSilnika
        self.mocKM = mocKM
        Samochod.LicznikSamochodow += 1
       

print(Samochod.LicznikSamochodow)
auto1 = Samochod("Ford", "Focus", "Benzyna", 180)
print(Samochod.LicznikSamochodow)
auto2 = Samochod("BMW", "X3", "Benzyna", 180)
print(Samochod.LicznikSamochodow)

auto1.wyswietl()