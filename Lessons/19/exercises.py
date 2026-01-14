lista1 = [32, 654, -201]
lista2 = [0, 111, 54]

print(f"Zadanie 1: {lista1} {lista2}")

lista3 = []
lista3.extend(lista1)
lista3.extend(lista2)

# Zadanie 2: Alternatywna metoda
# lista3 = lista1 + lista2

print(f"Zadanie 2: {lista3}")

lista3.pop(5)
lista3.pop(2)

print(f"Zadanie 3: {lista3}")

# Zadanie 4
# Wyszukiwanie elementw - min(), max()

min_element = min(lista3)
max_element = max(lista3)

while min_element in lista3:    
    lista3.remove(min_element)

while max_element in lista3:    
    lista3.remove(max_element)

print(f"Zadanie 4: {lista3}")

# Zadanie 5

lista3.append(100)

print(f"Zadanie 5: {lista3}")

# Zadanie 6

lista3.sort()

print(f"Zadanie 6: {lista3}")

# Zadanie 7

lista3_kopia = lista3.copy()

print(f"Zadanie 7: Oryginał {lista3} Kopia {lista3_kopia}")

# Zadanie 8

lista3_kopia.reverse()

print(f"Zadanie 8: Oryginał {lista3} Kopia {lista3_kopia}")

# Zadanie 9

for i in range(len(lista3_kopia)):
    lista3_kopia[i] += 1

for i in range(len(lista3)):
    lista3[i] -= 1

print(f"Zadanie 9 i 10: Oryginał {lista3} Kopia {lista3_kopia}")