"""
Stwórz funkcję dzielącą zdanie na wyrazy. Prawidłowe zdanie powinno zaczynać
się od wielkiej litery i kończyć kropką. W razie niespełnienia wymogów poprawnego
zdania podniesiony powinien zostać wyjątek z informacją o wymaganej korekcie.
"""


def zdanie_na_wyrazy(zdanie):
    try:
        if not zdanie[0].isupper():
            raise Exception("Zdanie zaczyna się małą literą")
        if not zdanie[-1] == ".":
            raise Exception("Zdanie nie kończy się kropką")
        
        print(zdanie.split(" "))
    except Exception as e:
        print(e)


# Dane testowe
zdanie_na_wyrazy("ala ma kota")
zdanie_na_wyrazy("Kuba ma kota")
zdanie_na_wyrazy("kuba ma psa.")
zdanie_na_wyrazy("Ala ma psa.")
