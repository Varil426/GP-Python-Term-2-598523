"""
Napisz program, który będzie działał jak książka telefoniczna.
Program poinien mieć następujące funkcje:
- Dodawanie nowego kontaktu - program powinien pytać użytkownika o imię i nazwisko oraz numer telefonu i dodać te dane do listy kontaktów.
Lista kontaktów powinna być przechowywana w postaci listy słowników, gdzie każdy słownik reprezentuje jeden kontakt.
- Sortowanie kontaktów za pomocą metody sortowania bąbelkowego - program powinien sortować listę kontaktów alfabetycznie według nazwisk z wykorzystaniem funkcji `bubble_sort`.
- Wyświetlanie listy kontaktów - program powinien wyświetlić listę kontaktów w formacie: "imię nazwisko - numer telefonu". Kontakty powinny być posortowane alfabetycznie według nazwisk.
"""

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j]["nazwisko"] > arr[j+1]["nazwisko"]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

kontakty = []

while True:
    print("1. Dodaj nowy kontakt")
    print("2. Wyświetl listę kontaktów")
    print("3. Wyjdź")
    wybor = input("Wybierz opcję: ")

    if wybor == "1":
        imie = input("Podaj imię: ")
        nazwisko = input("Podaj nazwisko: ")
        numer = input("Podaj numer: ")
        kontakt = {"imie": imie, "nazwisko": nazwisko, "numer": numer}
        kontakty.append(kontakt)
        bubble_sort(kontakty)
        print("Kontakt został dodany")
    elif wybor == "2":
        if len(kontakty) == 0:
            print("Brak kontaktów")
        else:
            print("Lista kontaktów:")
            for kontakt in kontakty:
                print(f"{kontakt["imie"]} {kontakt["nazwisko"]}: {kontakt["numer"]}")
    else:
        exit()