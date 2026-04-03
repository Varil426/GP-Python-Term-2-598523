"""
Korzystając z przygotowanej funkcji `add(a,b)` która czeka jedną sekundę, a następnie wyświetla wynik dodawania liczb `a` i `b`.
Utwórz dekorator `@timeline` który wyświetli czas wywołania funkcji oraz czas zakończenia jej pracy.
"""

import time


def add(a, b):
    time.sleep(1)
    print(a + b)


add(1, 5)
