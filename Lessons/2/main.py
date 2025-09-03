from Uzytkownik import Uzytkownik
from Przedmiot import Przedmiot
import random

users = []

# user1 = Uzytkownik()
# user1.imie = "Bartek"
# user1.nazwisko = "Kręgielewski"
# user1.wiek = 26

# users.append(user1)

# user1 = Uzytkownik()
# user1.imie = "Leonard"
# user1.nazwisko = "R"
# user1.wiek = 13

# users.append(user1)

def generujUzytkownika():
    lista_imion = ["Michał", "Piotrek", "Asia", "Jakub", "Tymon", "Bartek"]
    lista_nazwisk = ["Kowalski", "Piotrkowski", "Adamczyk", "Małysz", "Nowak"]
    wybrane_imie = random.choice(lista_imion)
    wybrane_nazwisko = random.choice(lista_nazwisk)
    wybrany_wiek = random.randint(13, 100)
    user = Uzytkownik()
    user.imie = wybrane_imie
    user.nazwisko = wybrane_nazwisko
    user.wiek = wybrany_wiek
    return user

for _ in range(15):
    users.append(generujUzytkownika())

for user in users:
    user.wyswietl()

# Zadanie 1 - Testy
print("================ Zadanie 1 - Testy ================")
testowy_user = users[0]
testowy_user.wyswietl()
testowy_user.zmien_wiek(66)
testowy_user.wyswietl()

# Zadanie 2 - Testy
print("================ Zadanie 2 - Testy ================")

mat = Przedmiot()
mat.zmien_nazwe("Matematyka")
mat.wyswietl_oceny()
mat.dodaj_ocene(6)
mat.dodaj_ocene(4)
mat.wyswietl_oceny()
mat.wyswietl_srednia()