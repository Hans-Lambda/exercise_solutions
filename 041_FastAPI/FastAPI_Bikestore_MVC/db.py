from models import Bike, Client, Partner, Bill
import pickle


bikes = [
    Bike(id_="agaag", name="Adventure Pro", manufacturer="TREK", year="2002-06-20T10:05:05.559000+00:00"),
    Bike(id_="36hds", name="Bullshit Pro", manufacturer="Bulls", year="2017"),
    Bike(id_="alfi7", name="Standard DDR Gedöns", manufacturer="Diamant", year="1986"),
    Bike(id_="afna5", name="E-Bike", manufacturer="KTM", year="2002"),
    Bike(id_="alh47", name="Fuck Jeff Bezos", manufacturer="Amazon", year="666"),
    Bike(id_="afaf5", name="Shitty E-Bike", manufacturer="KTM", year="6969")
]

clients = []

partners = []

bills = []


class DataController:

    # load and save bikes
    def store_bikes(self):
        with open('data_bikes.pickle', 'wb') as file:
            pickle.dump(bikes, file)

    def load_bikes(self):
        try:
            with open('data_bikes.pickle', 'rb') as file:
                bikes_loaded = pickle.load(file)
                return bikes_loaded
        except FileNotFoundError:
            self.store_bikes()
            return []

    # load and save clients
    def store_clients(self):
        with open('data_clients.pickle', 'wb') as file:
            pickle.dump(clients, file)

    def load_clients(self):
        try:
            with open('data_clients.pickle', 'rb') as file:
                clients_loaded = pickle.load(file)
                return clients_loaded
        except FileNotFoundError:
            self.store_clients()
            return []

    # load and save partners
    def store_partners(self):
        with open('data_partners.pickle', 'wb') as file:
            pickle.dump(partners, file)

    def load_partners(self):
        try:
            with open('data_partners.pickle', 'rb') as file:
                partners_loaded = pickle.load(file)
                return partners_loaded
        except FileNotFoundError:
            self.store_partners()
            return []

    # load and save bills
    def store_bills(self):
        with open('data_bills.pickle', 'wb') as file:
            pickle.dump(bills, file)

    def load_bills(self):
        try:
            with open('data_bills.pickle', 'rb') as file:
                bills_loaded = pickle.load(file)
                return bills_loaded
        except FileNotFoundError:
            self.store_bills()
            return []


data_controller = DataController()
bikes = data_controller.load_bikes()
clients = data_controller.load_clients()
partners = data_controller.load_partners()
bills = data_controller.load_bills()
