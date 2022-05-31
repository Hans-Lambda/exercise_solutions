import db
from datetime import datetime as dt


class Bike:

    def __init__(self, age, manufacturer, type, partner):

        self.age = age
        self.manufacturer = manufacturer
        self.type = type
        self.partner = partner
        self.status = "AVAILABLE"


class RentManagement:

    def __init__(self):
        pass

    def add_bikes(self, bike):
        db.bikes.append(bike)

    def remove_bikes(self, bike):
        db.bikes.remove(bike)

    def choose_bike(self):
        # ToD: implement
        return self.bike

    def choose_billing_method(self):
        # ToD: Implement
        choice = input("Please choose a billing method: ")

        return self.billing_method

    def rent(self, client, bike):

        billing_method = self.choose_billing_method()
        new_bill = Bill(client, bike.partner, bike, billing_method)
        Bill.open_bill(new_bill)
        Bill.print_bill(new_bill)

    def return_bycicle(self):
        id = input("Please provide contract ID: ")
        for bill in db.rents:
            if id == bill.id:
                Bill.close_bill(bill)
        else:
            print("Not a valid ID")

    def bycicles_list(self):
        for bike in db.bikes:
            print(f"Type: {bike.type}, Age: {bike.age}, Manufacturer: {bike.manufacturer}, Status: {bike.status}")

    def bills_list(self):
        for bill in db.rents:
            Bill.print_bill(bill)


class Bill:

    def __init__(self, client, partner, bike, billing_method):

        self.status = "Pending"
        self.partner = partner
        self.client = client
        self.bike = bike
        self.billing_method = billing_method
        self.date = dt.now()
        self.id = f"{partner[0]}{client[0]}{bike[0]}"       # or something else


    def open_bill(self, bill):
        for bike in db.bikes:
            if bill.bike == bike:
                bike.status = "NOT AVAILABLE"
        db.rents.append(bill)

    def close_bill(self, bill):
        for open_bill in db.rents:
            if bill == open_bill:
                open_bill.status = "CLOSED"
                used = open_bill.bike
        for bike in db.bikes:
            if used == bike:
                bike.status = "AVAILABLE"

    def print_bill(self, bill):
        print(f"Status: {bill.status}, Client: {bill.client}, Partner: {bill.partner}, Bike: {bill.bike}, "
              f"Billing Method: {bill.billing_method}, Date of Contract: {bill.date}")


class BillingMethod:

    def __init__(self):

        billing_method = None

    def pay_by_km(self):
        billing_method = "Pay by KM"
        return billing_method

    def pay_by_days(self):
        billing_method = "Pay by Day"
        return billing_method

    def pay_by_hour(self):
        billing_method = "Pay by Hour"
        return billing_method


class Person:

    def __init__(self, name, address, bank_account):

        self.name = name
        self.address = address
        self.bank_account = bank_account


class Client(Person):

    def __init__(self, name, address, bank_account):
        super().__init__(name, address, bank_account)

        self.rental_contracts = []


class Partner(Person):

    def __init__(self, name, address, bank_account):
        super().__init__(name, address, bank_account)

        self.bikes = []


class ClientManagement:

    def __init__(self, client):
        self.client = client

    def get_client(self):
        #ToD imnplement
        return client

    def add_client(self, client):
        db.clients.append(client)

    def remove_client(self, client):
        db.clients.remove(client)

    def login(self):
        pass



class PartnerManagement:

    def __init__(self, partner):
        self.partner = partner

    def add_partner(self, partner):
        db.partners.append(partner)

    def remove_partner(self, partner):
        db.partners.remove(partner)

