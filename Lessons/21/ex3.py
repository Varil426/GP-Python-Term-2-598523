"""
Na podstawie listy z temperaturą podaną w stopniach Fahrenhaita,
stwórz listę zawierającą te same temperatury w stopniach Celcjusza.

Przeliczanie ze stopni Fahrenhaita na Celcjusza odbywa się według wzoru:
C = (F - 32) * 5/9
"""

stopnie_fahrenheit = [32, 68, 104, 140]

wynik = [(f-32)*5/9 for f in stopnie_fahrenheit]
print(wynik)