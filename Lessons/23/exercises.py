import numpy as np
from numpy import random


def print_ex(exercise_number: int):
    separator_length = 80
    print("-" * separator_length)
    print(f"\n\nZadanie {exercise_number}\n\n")
    print("-" * separator_length)

"""
Zadanie 1

Stwórz funkcję `print_array()` w której zostanie stworzona dwuwymiarowa tablica - `ndarray` oraz wyświetlone zostaną:
a) Tablica,
b) Pierwszy element tablicy,
c) Pierwszy zagnieżdżony element tablicy,
d) Typ utworzonego obiektu,
e) Kształt utworzonego obiektu.

Funkcja powinna zwrócić utworzoną tablicę.

"""

print_ex(1)

# Miejsce na kod - Zadanie 1

def print_array():
    arr = np.array([[-1,2,-3],[4,5,6],[7,8,9],[10, 11, 12]])
    print(f"Tablica:\n{arr}")
    print(f"Pierwszy element tablicy: {arr[0]}")
    print(f"Pierwszy zagnieżdżony element tablicy: {arr[0][0]}") # Alternatywnie arr[0, 0]
    print(f"Typ tablicy: {type(arr)}")
    print(f"Kształt tablicy: {arr.shape}")

    return arr


arr = print_array()

# Koniec miejsca na kod - Zadanie 1

"""
W zadaniu 1 stworzyliśmy tablicę 4x3, także w zadaniu 2, nie będzie 9 elementów, a 12.
"""

"""
Zadanie 2

Stwórz funkcję `shapeshifter(arr)` która przyjmuje jako argument utworzoną wcześniej tablicę. Funkcja powinna:
a) zmienić rozmiar tablicy na 9x1,
b) zmienić rozmiar tablicy na 1x9,
c) zmienić rozmiar tablicy na 3x3,
d) zmienić rozmiar tablicy na -1x9,
e) zmienić rozmiar tablicy na 3x-1,
f) podzielić tablicę na 3 nowe tablice.

Wyświetl tablicę na każdym etapie.

"""

print_ex(2)

# Miejsce na kod - Zadanie 2

def shapeshifter(arr):
    print("Kształt tablicy 12x1")
    print(arr.reshape(12,1))
    print("Kształt tablicy 1x12")
    print(arr.reshape(1,12))
    print("Kształt tablicy 3x4 i 4x3")
    print(arr.reshape(3,4))
    print(arr.reshape(4,3))
    print("Kształt tablicy -1x12")
    print(arr.reshape(-1,12))
    print("Kształt tablicy 6x-1")
    print(arr.reshape(6,-1))
    print("Podział tablicy na 3")
    flattenarr = arr.flatten()
    print(flattenarr)
    newarr = np.array_split(flattenarr, 3)
    print(newarr)


shapeshifter(arr)

# Koniec miejsca na kod - Zadanie 2

"""
Zadanie 3

Utwórz funkcję `data_format`, która zawierać będzie tablicę zawierającą dane
różnych typów - wcześniej wspomniane zostało że tablice mogą przechowywać dane
tylko 1 typu, dlatego należy obsłużyć ewentualny wyjątek.
Dodatkowo utwórz tablice w których dane rzutowane będą kolejno na `string`i, `int`y i `float`y.

"""

print_ex(3)

# Miejsce na kod - Zadanie 3

def print_array_and_type(arr):
    print(arr)
    print(type(arr))

def data_format():
    try:
        arr = np.array([1, 123.32, "123"], dtype="i")
        print_array_and_type(arr)
        arr = np.array([1, 123.32, "123", "Bartek"], dtype="U")
        print_array_and_type(arr)
        arr = np.array([1, 123.32, "123", "Bartek"], dtype="f")
        print_array_and_type(arr)
    except Exception as e:
        print(e)

data_format()

# Koniec miejsca na kod - Zadanie 3

"""
Zadanie 4

Utwórz funkcję `sorted_ndarray` w której utworzona zostanie tablica, a następnie
wyświetlona, oraz posortowana i ponownie wyświetlona.

"""

print_ex(4)

# Miejsce na kod - Zadanie 4

def sorted_ndarray():
    arr = np.array([[5,2,9],[8,1,4],[3,7,6]])
    print(f"Tablica przed sortowaniem: {arr}")
    print(f"Tablica po sortowaniu: {np.sort(arr)}")

sorted_ndarray()

# Koniec miejsca na kod - Zadanie 4

"""
Zadanie 5

Stwórz funkcję `generate_random_numbers` która wygeneruje 10 losowych liczb
całkowitych od 0 do 100, oraz 10 losowych liczb typu float z zakresu od 0 do 1.

"""

print_ex(5)

# Miejsce na kod - Zadanie 5

def generate_random_numbers():
    for _ in range(10):
        print(random.randint(100))
    for _ in range(10):
        print(random.rand())

generate_random_numbers()


# Koniec miejsca na kod - Zadanie 5

"""
Zadanie 6

Stwórz funkcję `pick_random_numbers` która:
a) wygeneruje tablicę losowych liczb z zakresu od 0 do 1 o wymiarach 3x5,
b) wybierze losową liczbę ze zbioru liczb 3, 5, 7, 9,
c) utworzy tablicę o wymiarach 3x5 z losowych elementów ze zbioru liczb 3, 5, 7, 9,
d) wygeneruje 100 losowych liczb, korzystając ze zbioru liczb 3, 5, 7, 9, gdzie szansa na 3 wynosi 10%, na 5-30 %, na 7-60%, a na 9-0%.

"""

print_ex(6)

# Miejsce na kod - Zadanie 6

def pick_random_numbers():
    print(random.rand(3,5))
    print(random.choice([3,5,7,9]))
    print(random.choice([3,5,7,9], size=(3,5)))
    print(random.choice([3,5,7,9], p=[0.1,0.3,0.6,0], size=(100)))

pick_random_numbers()

# Koniec miejsca na kod - Zadanie 6

"""
Zadanie 7

Stwórz funkcję `shuffle_ndarray` w której przemieszasz tablicę oraz utworzysz permutację tablicy.
Permutacja - zmiana kolejności elementów w tablicy.

"""

print_ex(7)

# Miejsce na kod - Zadanie 7

# Koniec miejsca na kod - Zadanie 7

"""
Zadanie 8

Stwórz funkcję `array_functions` w której:
a) wygenerujesz tablicę z 11 wartościami równo rozmieszczonymi na przedziale od 0 do 10,
b) wyświetlisz tą tablicę,
c) wyświetlisz sumę elementów tej tablicy,
d) wyświetlisz najmniejszy element tablicy,
e) wyświetlisz największy element tablicy,
f) wyświetlisz średnią wartość tablicy,
g) wyświetlisz wariancje elementów tablicy,
h) wyświetlisz odchylenie standardowe elementów tablicy.

Wariacja - miara rozproszenia danych wokół średniej arytmetycznej.
Odchylenie standardowe - miara rozproszenia wyników średniej arytmetycznej, ukazująca jak bardzo wartości w zestawie danych różnią się od średniej arytmetycznej tych danych.

"""

print_ex(8)

# Miejsce na kod - Zadanie 8

# Koniec miejsca na kod - Zadanie 8

"""
Zadanie 9

Utwórz funkcję `mathematical_functions` w której:
a) wyświetlisz wartość liczby pi,
b) wyświetlisz wartość liczby eulera,
c) wyświetlisz wartość kwadratu liczby eulera,
d) wyświetlisz wartość sinus pi/2,
e) wyświetlisz wartość cosinus pi/2,
f) wyświetlisz wartość tangens pi/2,
g) wyświetlisz wartość pi/2 zamienioną na stopnie i 360 stopni zamienioną na radiany.

"""

print_ex(9)

# Miejsce na kod - Zadanie 9

# Koniec miejsca na kod - Zadanie 9
