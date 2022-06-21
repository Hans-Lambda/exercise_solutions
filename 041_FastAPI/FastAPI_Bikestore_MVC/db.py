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

    # def store_data(self, type_):
    #     with open(f'{type_}.pickle', 'wb') as file:
    #         pickle.dump(type_, file)
    #
    # def load_data(self, type_, error_data_dump=[]):
    #
    #     try:
    #         with open(f'{type_}', 'rb') as file:
    #             return pickle.load(file)
    #     except FileNotFoundError:
    #         self.store_data(error_data_dump)
    #         return []


    # load and save bikes
    def load_bikes(self):
        with open('data_bikes.pickle', 'rb') as file:
            bikes_loaded = pickle.load(file)
            return bikes_loaded

    def store_bikes(self):
        with open('data_bikes.pickle', 'wb') as file:
            pickle.dump(bikes, file)

    # load and save clients
    def load_clients(self):
        with open('data_clients.pickle', 'rb') as file:
            clients_loaded = pickle.load(file)
            return clients_loaded

    def store_clients(self):
        with open('data_clients.pickle', 'wb') as file:
            pickle.dump(clients, file)

    # load and save partners
    def load_partners(self):
        with open('data_partners.pickle', 'rb') as file:
            partners_loaded = pickle.load(file)
            return partners_loaded

    def store_partners(self):
        with open('data_partners.pickle', 'wb') as file:
            pickle.dump(partners, file)

    # load and save bills
    def load_bills(self):
        with open('data_bills.pickle', 'rb') as file:
            bills_loaded = pickle.load(file)
            return bills_loaded

    def store_bills(self):
        with open('data_bills.pickle', 'wb') as file:
            pickle.dump(bills, file)


data_controller = DataController()
bikes = data_controller.load_bikes()
clients = data_controller.load_clients()
partners = data_controller.load_partners()
bills = data_controller.load_bills()
