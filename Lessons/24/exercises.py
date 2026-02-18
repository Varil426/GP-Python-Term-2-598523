import cv2
from PIL import Image
import numpy as np
import os

# Ustawienie katalogu roboczego
os.chdir(os.path.dirname(os.path.abspath(__file__)))


# Wyświetlanie grafiki
def show_image(img):
    cv2.imshow("image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Wczytanie grafiki z pliku
def read_image_cv(path):
    img = cv2.imread(path, cv2.IMREAD_COLOR)
    print(img)
    print(img.shape)
    print(type(img))
    show_image(img)
    return img


def read_image_PIL(path):
    img = Image.open(path)
    try:
        print(img)
    except:
        print(type(img))
    img.show()
    return img


image = read_image_cv("image.jpg")
# read_image_PIL("image.jpg")

def reverse_image(img):
    # Obrócenie góra dół
    new_img = []
    for row in range(img.shape[0]):
        new_row = []
        for column in range(img.shape[1]):
            new_row.append(img[-1-row][column])
        new_img.append(new_row)
    return np.array(new_img)

show_image(reverse_image(image))

def reverse_image_short(img):
    img_reverse = img[::-1]
    return img_reverse

show_image(reverse_image_short(image))

show_image(cv2.flip(image, 0))

def gray_scale(img):
    img_copy = img.copy()
    for row in range(img_copy.shape[0]):
        for column in range(img_copy.shape[1]):
            gray = int(sum(img_copy[row][column])/3)
            img_copy[row][column][0] = gray
            img_copy[row][column][1] = gray
            img_copy[row][column][2] = gray
    return np.array(img_copy)

show_image(gray_scale(image))
show_image(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY))

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
