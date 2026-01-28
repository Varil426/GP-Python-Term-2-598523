"""
Na podstawie listy krotek zawierającej długości boków trójkąta stwórz listę
zawierającą tylko krotki z których można skonstruować trójkąt.

Jaki był warunek aby z trzech odcinków można było zbudować trójkąt?
"""

trojkaty = [(1, 3, 5), (2, 2, 3), (3, 1, 8), (3, 4, 5)]

# krotka_testowa = (10,15,20)
# print(max(krotka_testowa))
# print(sum(krotka_testowa) - max(krotka_testowa))

wynik = [trojkat for trojkat in trojkaty if sum(trojkat) - max(trojkat) > max(trojkat)]
print(wynik)
