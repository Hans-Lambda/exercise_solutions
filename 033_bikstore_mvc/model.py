import uuid
import datetime as dt


class User:

    def __init__(self, name, username, password):

        self.name = name
        self.username = username
        self.password = password
        self.client = False
        self.partner = False


class Bike:

    def __init__(self, age, manufacturer, type_, partner):

        self.age = age
        self.manufacturer = manufacturer
        self.type_ = type_
        self.partner = partner
        self.status = "AVAILABLE"
        self.id = str(uuid.uuid4())[:5]


class Bill:

    def __init__(self, bike, client, billing_method, price):

        self.bike = bike
        self.client = client
        self.date = dt.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        self.billing_method = None
        self.id = uuid.uuid4()
        self.status = "Pending"
        self.price = None
