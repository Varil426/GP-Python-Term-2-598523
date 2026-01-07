gra = {
    'nazwa_gry': "Dead By Daylight",
    'data_wydania': 2016,
    'wydawca': "Behaviour Interactive",
    'gatunek': ["Horror", "Survival", "Multiplayer", "Co-Op"]
}

print(gra.get("nazwa_gry"))

def pretty_print(dic):
    print("Słownik:")
    for key in dic.keys():
        print(f"\t{key}: {dic.get(key)}")

# pretty_print(gra)

# from pprint import pprint

# print("Zwykły print:")
# print(gra)

# print("pprint:")
# pprint(gra)

import json
import os
from pprint import pprint

os.chdir(os.path.dirname(os.path.abspath(__file__)))

spis_gier = {}
with open("l1.json", "r") as file:
    spis_gier = json.load(file)

pprint(spis_gier)

spis_gier.get("spis_gier").append(gra)

pprint(spis_gier)

with open("l1_2.json", "w") as file:
    json.dump(spis_gier, file, indent=4, sort_keys=True)