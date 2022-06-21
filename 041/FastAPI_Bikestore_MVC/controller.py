import re
import db
import datetime
import uuid
from models import Client, Partner, Bike, Bill

bikes = db.bikes
clients = db.clients
partners = db.partners
bills = db.bills


class BikeController:

    def list_bikes(self):
        return bikes

    def list_bikes_by_manufacturer(self, manufacturer):

        return [bike for bike in bikes if re.findall(manufacturer.lower(), bike.manufacturer.lower())]

    def list_bikes_by_name(self, name):

        return [bike for bike in bikes if re.findall(name.lower(), bike.name.lower())]

    def add_bike(self, bike):

        bikes.append(bike)

    def remove_bike(self, id_: str):

        [bikes.remove(bike) for bike in bikes if id_ == bike.id_]


class ClientController:

    def list_clients(self):
        return clients

    def list_clients_by_bill(self, id_: str):
        return [bill.client for bill in bills if bill.client.id_ == id_]

    def list_clients_by_name(self, name):
        return [client for client in clients if re.findall(name.lower(), clients.client.name.lower())]

    def add_client(self, client):
        clients.append(client)

    def modify_client(self, email: str):
        for client in clients:
            if email == client.email:
                client.name = input("Please input new name")
                client.email = input("Please input new email address")
                client.username = input("Please input new username")
                client.password = input("Please input new password")

    def remove_client(self, email):
        [client.remove() for client in clients if clients.client.email == email]


class PartnerController:

    def list_partners(self):
        return partners

    def list_partners_by_bill(self, id_: str):
        return [bill.partner for bill in bills if bill.partner.id_ == id_]

    def list_partners_by_bike(self, id_: str):
        return [bike.partner for bike in bikes if bike.partner.id_ == id_]

    def list_partners_by_name(self, name):
        return [partner for partner in partners if re.findall(name.lower(), partners.partner.name.lower())]

    def add_partner(self, partner):
        partners.append(partner)

    def modify_partner(self, email):
        for partner in partners:
            if email == partner.email:
                partner.name = input("Please input new name")
                partner.email = input("Please input new email address")
                partner.username = input("Please input new username")
                partner.password = input("Please input new password")


    def remove_partner(self, email):
        [partner.remove() for partner in partners if partners.partner.email == email]


class BillingController:

    def get_bills(self):
        return [bill for bill in bills]

    def get_open_bills(self):
        return [bill for bill in bills if bill.status == "OPEN"]

    def get_closed_bills(self):
        return [bill for bill in bills if bill.status == "CLOSED"]

    def get_bill_by_id(self, id_):
        return [bill for bill in bills if bills.bill.id_ == id_]

    def get_bills_by_bike(self, id_):
        return [bill for bill in bills if bills.bike.id_ == id_]

    def get_bills_by_partner(self, email):
        return [bill for bill in bills if bills.partner.email == email]

    def get_bills_by_client(self, email):
        return [bill for bill in bills if bills.client.email == email]

    def new_bill(self, client, bike, billing_method, billing):

        bill = Bill()
        self.bike = bike
        self.partner = bike.partner
        self.date = datetime.datetime.now()
        self.id_ = str(uuid.uuid4())[4]
        self.billing_method = billing_method
        self.status = "OPEN"
        self.billing = billing

        bills.append(bill)
