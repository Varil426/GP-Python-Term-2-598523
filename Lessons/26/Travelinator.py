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
    response=requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={API_KEY}')
    print(response.status_code)
    pprint(response.json())
    json = response.json()[0]
    lat = json['lat']
    lon = json['lon']
    city = json['name']
    country = json['country']
    return lat, lon, city, country

def get_weather_info(lat, lon, API_KEY):
    response=requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&limit=1&appid={API_KEY}&lang=PL&units=metric')
    json = response.json()
    weather = json['weather'][0]['description']
    temp = json['main']['temp']
    pressure = json['main']['pressure']
    humidity = json['main']['humidity']
    return weather, temp, pressure, humidity

# check_coordinates("Warszawa", API_KEY)

# Logika programu
print("Witaj, jestem Travelinator, twój inteligentny asystent podróży")
origin_city = input("Podaj nazwę miasta z którego podróżujesz: ")
destination_city = input("Podaj nazwę miasta do którego podróżujesz: ")

origin_lat, origin_lon, origin_city, origin_country = check_coordinates(origin_city, API_KEY)
destination_lat, destination_lon, destination_city, destination_country = check_coordinates(destination_city, API_KEY)

weather, temperature, pressure, humidity = get_weather_info(destination_lat, destination_lon, API_KEY)

print(f"Miasto z którego podróżujesz: {origin_city}")
print(f"Miasto do którego podróżujesz: {destination_city}")
print(f"Jego współrzędne geograficzne to:\n({destination_lat}, {destination_lon})")
print(f"Podogda: {weather}")
print(f"Temperatura: {temperature} stopni Celcjusza")
print(f"Wilgotność: {humidity}%")
print(f"Ciśnienie atmosferyczne: {pressure}hPa")