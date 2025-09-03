class Przedmiot:
    nazwa = ""
    oceny = []
    srednia = 0

    def zmien_nazwe(self, nowa_nazwa):
        self.nazwa = nowa_nazwa

    def dodaj_ocene(self, ocena):
        self.oceny.append(ocena)
        # Aktualizacja średniej
        self.srednia = sum(self.oceny) / len(self.oceny)

    def wyswietl_oceny(self):
        if len(self.oceny) == 0:
            print("Nie masz jeszcze żadnych ocen")
            return

        oceny_str = []
        for ocena in self.oceny:
            oceny_str.append(str(ocena))

        print(f"Twoje oceny to: {", ".join(oceny_str)}")

    def wyswietl_srednia(self):
        print(f"Twoja średnia to: {self.srednia}")
