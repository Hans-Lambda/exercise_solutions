
class Person:

    def __init__(self, name, email):
        self.name = name
        self.email = email


class Client(Person):

    def __init__(self, id, name, email, address) :
        super().__init__(name, email)
        self.id = id
        self.address = address


class Partner(Person):

    def __init__(self, name, email, bike):
        super().__init__(name, email)
        self.bike = bike


class Bike:

    def __init__(self, type, manufacturer, year):
        self.type = type
        self.manufacturer = manufacturer
        self.year = year
        self.status = "AVAILABLE"


class Bill:

    def __init__(self, client, partner, bill_strategy):
        self.status = "PENDING"
        self.client = client
        self.partner = partner
        self.bill_strategy = bill_strategy
        self.total_price = 0
