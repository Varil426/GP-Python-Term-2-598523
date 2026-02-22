"""
Korzystając z pliku `dane.txt` wykonaj następujące zadania:
1. Znajdź wszystkie adresy email.
2. Znajdź wszystkie osoby zaproszone na spotkania (Imie + Nazwisko).
3. Znajdź wszystkie numery telefonów.
4. Zamień wszystkie numery telefonów na xxx - xxx - xxx.
5. Znajdź pierwszą datę.
6. Znajdź wszystkie godziny, o których rozpoczynają się spotkania.
7. Sprawdź, ile spotkań zostało zaplanowanych.
"""

import os

os.chdir(os.path.dirname(__file__))

with open("dane.txt", "r", encoding="utf-8") as file:
    data = file.read()

print(f"{'='*30} Dane {'='*30}")

print(data)  # Test wczytania danych

print(f"{'='*30} Zadania {'='*30}")
