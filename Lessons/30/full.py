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
# order = [
#     {"size": "L", "pizza_amount": 1, "pizza_name": "Margherita"}
# ]  # Testowe zamówienie


def main_page():
    print("Witaj na stronie pizzeri u Vita")
    print("Wybierz co chcesz zrobić")
    print("1. Wyświetl menu")
    print("2. Dodaj pizze do zamówienia")
    print("3. Wyczyść zamówienie")
    print("4. Wyślij zamówienie")
    print("5. Zakończ")
    option = input("")
    if option == "1":
        display_menu()
    elif option == "2":
        add_to_order()
    elif option == "3":
        order.clear()
        main_page()
    elif option == "4":
        send_order()
        main_page()
    elif option == "5":
        quit()
    else:
        print("Podano złą opcję")


def display_menu():
    for pizza in list_of_pizzas:
        print(f"Pizza {pizza['pizza']}")
        print(f"Składniki {', '.join(pizza['dodatki'])}")
        print(
            f"Ceny: Mała: {pizza['ceny']['S']} zł     Średnia: {pizza['ceny']['M']} zł     Duża: {pizza['ceny']['L']} zł"
        )
        print(" ")
    input("Wciśnij enter aby wrócić do ekranu głównego")
    main_page()


def add_to_order():
    print("Którą pizzę chcesz zamówić: ")
    for pizza_name in list_of_pizzas_names:
        print(f"{list_of_pizzas_names.index(pizza_name)+1}.{pizza_name}")
    try:
        pizza_name_number = int(input("Podaj numer pizzy: "))
        if pizza_name_number > len(list_of_pizzas_names) or pizza_name_number < 1:
            print("Pizza o podanym numerze nie istnieje")
            time.sleep(1)
            main_page()
    except:
        print("Należy wprowadzić liczbę całkowitą")
        time.sleep(1)
        main_page()

    try:
        pizza_amount = int(input("Ile pizz chcesz zamówić: "))
        if pizza_amount < 1:
            print("Należy zamówić co najmniej jedną pizze")
            time.sleep(1)
            main_page()
        else:
            pass
    except:
        print("Należy wprowadzić liczbę całkowitą")
        time.sleep(1)
        main_page()

    size = input("Jakie rozmiary mają być pizze (S/M/L): ")
    if size.upper() not in "SML":
        print("Podano zły rozmiar pizzy")
        time.sleep(1)
        main_page()
    else:
        size = size.upper()

    order.append(
        {
            "size": size,
            "pizza_amount": pizza_amount,
            "pizza_name": list_of_pizzas_names[pizza_name_number - 1],
        }
    )
    print(
        f"Dodano {pizza_amount} x {list_of_pizzas_names[pizza_name_number-1]}[{size}] do zamowienia"
    )
    time.sleep(3)
    main_page()


def calculate_cost(ordered_pizza):
    for pizza in list_of_pizzas:
        if pizza["pizza"] == ordered_pizza["pizza_name"]:
            cost = int(ordered_pizza["pizza_amount"]) * int(
                pizza["ceny"][ordered_pizza["size"]]
            )
    return cost


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

    # with smtplib.SMTP(smtp_server, smtp_port, timeout=10) as server:
    with smtplib.SMTP_SSL(smtp_server, smtp_port, timeout=10) as server:
        # server.set_debuglevel(1)
        # server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, message.as_string())


def send_order():
    if not order:
        print("Nie można zrealizować pustego zamówienia")
        time.sleep(1)
        main_page()

    tekst = (
        "Dziękujemy za wybranie pizzeri u Vita, oto podsumowanie Twojego zamówinia:\n"
    )
    total_cost = 0
    for pizza in order:
        cost = calculate_cost(pizza)
        tekst += f"{pizza['pizza_amount']} x {pizza['pizza_name']}[{pizza['size']}] : {cost}zł\n"
        total_cost += cost
    tekst += f"Łączny koszt: {total_cost} zł"
    send_email(tekst)
    print("Zamówienie zostało złożone")
    input("Wciśnij enter aby kontynuować")


main_page()
