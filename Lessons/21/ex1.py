"""
Na podstawie podanej listy stwórz listę zawierającą same palindromy.
Palindrom to wyraz, który czytany od tyłu jest taki sam jak czytany od przodu.
"""

slowa = ["ala", "kot", "pies", "kamilslimak", "zebra", "madam", "Adam"]

wynik = [slowo for slowo in slowa if slowo == slowo[::-1]]
print(wynik)