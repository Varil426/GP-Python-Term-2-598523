import requests
from bs4 import BeautifulSoup
from fpdf import FPDF
import os

POKEDEX_URL = "https://pokemondb.net/pokedex/game/lets-go-pikachu-eevee"

# Ustawienie katalogu roboczego
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def scrap_pokemon_list():
    response = requests.get(POKEDEX_URL)
    # print(response.content)
    soup = BeautifulSoup(response.content, 'html.parser')
    pokemons_list = []
    cards_list = soup.find("div", class_="infocard-list")
    cards_data = cards_list.find_all("span", class_="infocard-lg-data")
    for data in cards_data:
        name = data.find('a')
        number = data.find('small')
        pokemon = (name.get_text(), number.get_text())
        pokemons_list.append(pokemon)

    return pokemons_list

def get_pokemon_info(name):
    name = name.replace("\'", '')
    name = name.replace(". ", '-')
    name = name.replace("♀", '-f')
    name = name.replace("♂", '-m')

    url = f'https://pokeapi.co/api/v2/pokemon/{name.lower()}'
    response = requests.get(url)
    return response.json()

def get_pokemon_image(pokemon_info):
    link = pokemon_info['sprites']['front_default']
    return link

def get_pokemon_types(pokemon_info):
    types = []
    for item in pokemon_info['types']:
        type = item['type']['name']
        types.append(type)
    return types

pokemon_list = scrap_pokemon_list()
# print(pokemon_list)

# for pokemon in pokemon_list:
#     try:
#         get_pokemon_info(pokemon[0])
#     except:
#         print(pokemon[0])

pdf = FPDF()
pdf.add_font("DejaVu", "", "DejaVuSans.ttf", uni=True)

# i = 0
for pokemon in pokemon_list:
    try:
        info = get_pokemon_info(pokemon[0])
        image = get_pokemon_image(info)
        types = get_pokemon_types(info)
    except:
        print(pokemon[0])
    else:
        pdf.add_page(format="A5")
        pdf.set_font("DejaVu", size=16)
        pdf.text(x=5, y=10, text=f"{pokemon[1]} {pokemon[0]}")
        pdf.image(image, x=30, y=10, w=100, h=100)
        pdf.set_font("DejaVu", size=12)
        type_tekst = ''.join(str(type) + ', ' for type in types)
        pdf.text(x = 50, y = 120, text=f"Typ: {type_tekst[:-2]}")

        # i+=1
        # if i > 15:
        #     break

pdf.output("pokedex.pdf")