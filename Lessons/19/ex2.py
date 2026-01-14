"""
Na listę `lista_gier` wkradł się błędy.
Napisz program, który usunie z niej wszystkie elementy, które nie są nazwami gier (czyli typu `str`).
"""

lista_gier = [
    False,
    "Valorant",
    None,
    1024,
    True,
    "Cyberpunk 2077",
    -42,
    None,
    "League of Legends",
    False,
    137,
    "The Witcher 3",
    True,
    666,
    "Minecraft",
    None,
    256,
    False,
    "Grand Theft Auto V",
    512,
    True,
    None,
    "Counter-Strike",
    -15,
    2048,
    "Elden Ring",
    88,
    None,
    0,
    True,
    999,
    "Fortnite",
    17,
    None,
    False,
    73,
    "Red Dead Redemption 2",
    -99,
    42,
    None,
]

poprawna_lista_gier = []

for element in lista_gier:
    if isinstance(element, str):
        poprawna_lista_gier.append(element)

print(poprawna_lista_gier)