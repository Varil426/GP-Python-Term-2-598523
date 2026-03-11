import requests
import json
import os
from pprint import pprint

# Asystent podróży
# Api pogodwe - https://openweathermap.org/api
# Api z informacjami o krajach - https://restcountries.com/
# Api z informacjami o kursach walut - https://api.nbp.pl/#info

# Ustawienie katalogu roboczego
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Wczytanie klucza API z pliku secrets.json
with open("secrets.json", "r") as file:
    secrets = json.load(file)
    API_KEY = secrets["API_KEY"]


def check_coordinates(city, API_KEY):
    response = requests.get(
        f"http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={API_KEY}"
    )
    print(response.status_code)
    pprint(response.json())
    json = response.json()[0]
    lat = json["lat"]
    lon = json["lon"]
    city = json["name"]
    country = json["country"]
    return lat, lon, city, country


def get_weather_info(lat, lon, API_KEY):
    response = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&limit=1&appid={API_KEY}&lang=PL&units=metric"
    )
    json = response.json()
    weather = json["weather"][0]["description"]
    temp = json["main"]["temp"]
    pressure = json["main"]["pressure"]
    humidity = json["main"]["humidity"]
    return weather, temp, pressure, humidity

def get_currency_code(country_code):
    url = f"https://restcountries.com/v3.1/alpha/{country_code.upper()}"
    response = requests.get(url)
    currency_code = list(response.json()[0]["currencies"].keys())[0]
    return currency_code


def get_country_full_name(country_code):
    url = f"https://restcountries.com/v3.1/alpha/{country_code.upper()}"
    # response = requests.get(url)
    # country_name = response.json()[0]["name"]["common"]
    # return country_name
    try:
        response = requests.get(url)
        country_name = response.json()[0]["name"]["common"]
    except:
        return country_code
    else:
        return country_name

def get_currency_ratio(ori_curr, dest_curr):
    if ori_curr != "PLN":
        url = f"http://api.nbp.pl/api/exchangerates/rates/A/{ori_curr.lower()}"
        reposne = requests.get(url)
        ori_ratio = reposne.json()['rates'][0]['mid']
    else:
        ori_ratio = 1

    if dest_curr != "PLN":
        url = f"http://api.nbp.pl/api/exchangerates/rates/A/{dest_curr.lower()}"
        reposne = requests.get(url)
        dest_ratio = reposne.json()['rates'][0]['mid']
    else:
        dest_ratio = 1

    ratio = float(ori_ratio)/float(dest_ratio)
    return ratio

def print_weather_info(place):
    lat, lon, _, _ = check_coordinates(place, API_KEY)
    w, t, p, h = get_weather_info(lat, lon)
    print(f"Pogoda dla miasta {place}: {w}")
    print(f"Temperatura: {t} st. Celcjusza")
    print(f"Ciśnienie: {p} hPa")
    print(f"Wilgotność: {h}%")

# check_coordinates("Warszawa", API_KEY)

# Logika programu
print("Witaj, jestem Travelinator, twój inteligentny asystent podróży")

origin_place = None
destination_place = None

while True:
    print("""Jaką akcję chcesz wykonać?
                1. Podaj/zmień miejsce startowe
                2. Podaj/zmień miejsce docelowe
                3. Sprawdź lokalizację miejsca startowego
                4. Sprawdź lokalizację miejsca docelowego
                5. Sprawdź pogodę miejsca startowego
                6. Sprawdź pogodę miejsca docelowego
                7. Dowiedz się więcej o walucie
                8. Koniec""")
    
    chosen_input = int(input())

    if chosen_input == 1:
        origin_place = input("Podaj miasto startowe.\n")
    elif chosen_input == 2:
        destination_place = input("Podaj miasto docelowe.\n")
    elif chosen_input == 3:
        if origin_place is not None:
            lat, lon, _, country = check_coordinates(origin_place, API_KEY)
            country_name = get_country_full_name(country)
            print(f"Miasto {origin_place} leży w kraju {country_name}\nDługość geograficzna: {lon}, szerokość geograficzna {lat}")
        else:
            print("Najpierw musisz podać miasto startowe")
    elif chosen_input == 4:
        if destination_place is not None:
            lat, lon, _, country = check_coordinates(destination_place, API_KEY)
            country_name = get_country_full_name(country)
            print(f"Miasto {destination_place} leży w kraju {country_name}\nDługość geograficzna: {lon}, szerokość geograficzna {lat}")
        else:
            print("Najpierw musisz podać miasto docelowe")
    elif chosen_input == 5:
        if origin_place is not None:
            print_weather_info(origin_place)
        else:
            print("Najpierw musisz podać miasto startowe")
    elif chosen_input == 6:
        if destination_place is not None:
            print_weather_info(destination_place)
        else:
            print("Najpierw musisz podać miasto docelowe")
    elif chosen_input == 7:
        pass
    elif chosen_input == 8:
        quit()
    else:
        print("Podano błędą akcję")
    print("Naciśniej entry aby kontynuować...")
    input()
