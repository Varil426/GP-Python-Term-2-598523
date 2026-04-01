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

def display_menu():
    for pizza in list_of_pizzas:
        print(f"Pizza {pizza["pizza"]}")
        print(f"Składniki {', '.join(pizza["dodatki"])}")
        print(f"Ceny: ")
        print(f"\tMała: {pizza["ceny"]["S"]} zł")
        print(f"\tŚrednia: {pizza["ceny"]["M"]} zł")
        print(f"\tDuża: {pizza["ceny"]["L"]} zł")
        print(" ")
    input("Wciśnij dowolny klawisz")
    main_page()

def add_to_order():
    print("Którą pizzę chcesz zamówić: ")
    for name in list_of_pizzas_names:
        print(f"{list_of_pizzas_names.index(name)+1}. {name}")
    pizza_name_choice = int(input("Podaj numer pizzy: "))
    pizza_amount = int(input("Ile pizz chcesz zamówić: "))
    size = input("Jakiego rozmiaru mają być pizze (S/M/L): ")
    order.append({
        "size": size,
        "pizza_amount": pizza_amount,
        "pizza_name": list_of_pizzas_names[pizza_name_choice-1]
        })
    print("Dodano do zamówienia")
    main_page()

def calculate_cost(ordered_pizza):
    for pizza in list_of_pizzas:
        if pizza["pizza"] == ordered_pizza["pizza_name"]:
            cost = int(ordered_pizza["pizza_amount"]) * int(pizza["ceny"][ordered_pizza["size"]])
    return cost

def send_order():
    tekst = "Dziękujemy za wybranie naszej pizzeri. Oto podsumowanie zamówienia:\n"
    total_cost = 0
    for pizza in order:
        cost = calculate_cost(pizza)
        tekst+=f"{pizza["pizza_amount"]} x {pizza["pizza_name"]}{pizza["size"]} : {cost} zł"
        total_cost += cost
    tekst += f"Łączny koszt: {total_cost} zł"
    # print(tekst)
    send_email(tekst)
    print("Zamówienie zostało złożone")
    main_page()

def send_email(message_txt):
    dotenv.load_dotenv()
    subject = "Pizzeria u Vita - potwierdzenia zamowienia"
    sender_email = os.getenv("sender_email")
    recipient_email = os.getenv("recipient_email")
    sender_password = os.getenv("sender_password")
    smtp_server = os.getenv("smtp_server")
    smtp_port = int(os.getenv("smtp_port"))

    message = MIMEMultipart()
    message["Subject"] = subject
    message["From"] = sender_email
    message["To"] = recipient_email
    body_part = MIMEText(message_txt)
    message.attach(body_part)

    with smtplib.SMTP_SSL(smtp_server, smtp_port, timeout=10) as server:
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, message.as_string())


def main_page():
    print("Witaj na stronie naszej pizzeri!")
    print("Wybierz co chcesz zrobić")
    print("1. Wyświetl menu")
    print("2. Dodaj pizze do zamówienia")
    print("3. Wyczyść zamówienie")
    print("4. Wyślij zamówienie")
    print("5. Zakończ")
    option = int(input(""))
    if option == 1:
        display_menu()
    elif option == 2:
        add_to_order()
    elif option == 3:
        order.clear()
        main_page()
    elif option == 4:
        send_order()
    elif option == 5:
        quit()
    else:
        print("Podano złą opcję")
        main_page()

main_page()