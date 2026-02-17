import cv2
from PIL import Image
import numpy as np
import os

# Ustawienie katalogu roboczego
os.chdir(os.path.dirname(os.path.abspath(__file__)))


# Wyświetlanie grafiki
def show_image(img):
    pass


# Wczytanie grafiki z pliku
def read_image_cv(path):
    pass


def read_image_PIL(path):
    pass


image = read_image_cv("image.jpg")


# Zadania

"""
Napisz funkcję change_colors, która przyjmuje 4 argumenty:
- img - obraz w formacie np.array,
- R_scale - współczynnik zmiany koloru czerwonego piksela,
- G_scale - współczynnik zmiany koloru zielonego piksela,
- B_scale - współczynnik zmiany koloru niebieskiego piksela.

Funkcja powinna dla każdego piksela ustalać nową wartość koloru jako stara wartość
razy współczynnik dla odpowiedniej barwy oraz zwrócić przefiltrowany obraz.
"""


def change_colors(img, R_scale, G_scale, B_scale):
    pass


show_image(change_colors(image, 1.4, 0, 0))

"""
Stwórz funkcję binaryzacji, która na podstawie wartości piksela w skali szarości
ustawia go na kolor biały lub czarny. Próg graniczny (treshold) podawany jest jako
argument funkcji.
"""


def tresholding(img, treshold):
    pass


show_image(tresholding(image, 200))
