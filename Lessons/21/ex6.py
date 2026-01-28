"""
Napisz funkcję `dodawanie`, która przyjmuje dwa argumenty: `a` i `b` oraz wyświetla ich sumę.
Co się wydarzy jeżeli jako argument podamy `int`a i `str`inga?
Jak poprawnie obsłużyć taki wyjątek?
"""


def dodawanie(a, b):
    try:
        print(f"Wynik dodawania {a} + {b} = {a+b}")
    except TypeError:
        print("Typy nie są zgodne")


# Dane testowe
dodawanie("5", 5)
dodawanie(5, 5)
dodawanie("5", "5")
