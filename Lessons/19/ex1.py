"""
Napisz program w którym stworzysz listę z 10 liczbami, a następnie wypiszesz co drugą z nich.
"""

lista = [1,2,3,4,5,6,7,8,9,10]

# Sposób 1
for index in range(len(lista)):
    reszta = index % 2
    if reszta == 0:
        print(lista[index])

# Sposób 2
for index in range(0, len(lista), 2):
    print(lista[index])