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
