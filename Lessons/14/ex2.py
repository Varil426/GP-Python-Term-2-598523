"""
Utwórz symulator kolejki do kina, gdzie elementami kolejki są klienci razem z ich zamówieniem.
Do utworzenia symulatora kolejki użyj naszej struktury `Queue`, którą stworzyliśmy wcześniej.
"""

from Queue import Queue

class Customer:
    def __init__(self, name, order):
        self.name = name
        self.order = order

class CinemaQueue:
    def __init__(self):
        self.queue = Queue()

    def is_empty(self):
        return self.queue.is_empty()
    
    def add_customer(self, customer: Customer):
        self.alert_employee("New customer!")
        self.queue.enqueue(customer)

    def remove_customer(self):
        if not self.is_empty():
            return self.queue.dequeue()
    
    def next_customer_order(self):
        if not self.is_empty():
            next_customer = self.queue.peek()
            return next_customer.order
        
    def alert_employee(self, alert_text):
        print(f"ALERT: {alert_text}")

# Testy

queue = CinemaQueue()

queue.add_customer(Customer("Anna", "popcorn"))
queue.add_customer(Customer("Tomasz", "cola"))
queue.add_customer(Customer("Marta", "hot dog"))

while not queue.is_empty():
    next_customer = queue.remove_customer()
    print(f"Obsługujemy: {next_customer.name}, który/a zamówił/a {next_customer.order}")

    if not queue.is_empty():
        next_order = queue.next_customer_order()
        print(f"Następny klient zamówił {next_order}\n")
