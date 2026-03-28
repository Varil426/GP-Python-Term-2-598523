import json
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import dotenv

# Ustawienie katalogu roboczego
os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open("menu.json", "r", encoding="utf-8") as file:
    menu = json.load(file)
list_of_pizzas = menu["menu"]

list_of_pizzas_names = []
for pizza in list_of_pizzas:
    list_of_pizzas_names.append(pizza["pizza"])

order = []
