"""
Napisz program przedstawiający postać z gry RPG.
Program powinien wypisać nazwę postaci składającą się z dowolnej liczby imion i przydomków podanych do funkcji jako argumenty nienazwane oraz dowolną liczbę klas wraz z ich poziomami, które zostaną przekazane do funkcji jako argumenty nazwane.
"""


def create_hero(*args, **kwargs):
    name = " ".join(args)

    classes = "\n".join(f"Klasa: {cls}, lvl: {lvl}" for cls, lvl in kwargs.items())

    hero_description = f"Imię bohatera: {name}\n{classes}"

    return hero_description


print(create_hero("Jurand", "Posępny", "Okrutny", "Mroczny", Paladyn=10, Mag=2))
