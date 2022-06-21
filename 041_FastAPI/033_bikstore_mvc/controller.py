from model import User, Bike, Bill
import db


class UserController:

    active_user = None

    def login_user(self, username, password):

        for user in db.users:
            if user.username == username and user.password == password:
                self.active_user = user
                return True

    def register(self, name, username, password):

        user = User(name, username, password)
        db.users.append(user)
        self.active_user = user


class BikeController:

    def add_bike(self, age, manufacturer, type_, partner):

        bike = Bike(age, manufacturer, type_, partner)
        db.bikes.append(bike)

    def get_bike_search(self, searchterms):

        search = db.bikes
        for term in searchterms:
            search = [bike for bike in db.bikes if bike.type.find(term) != -1 or bike.age.find(term) != -1
                      or bike.manufacturer.find(term) != -1 or bike.id.find(term) != -1]
        return search

    def get_bike_by_id(self, id):

        choice = None
        for bike in db.bikes:
            if id == bike.id:
                if bike.status == "AVAILABLE":
                    choice = bike
                else:
                    print("This bike is not available! try again!")
        if not choice:
            print("Incorrect ID, try again!")
        else:
            return choice

    def list_bikes(self):

        for bike in db.bikes:
            print(f"Type: {bike.type_}, Manufacturer: {bike.manufacturer}, Age: {bike.age}, Status: {bike.status}, Bike ID: {bike.id}")


class BillingController:

    total = 0

    def create_bill(self, bike, client, billing_method, price):

        bill = Bill(bike, client, billing_method, price)
        bike.status = "NOT AVAILABLE"
        db.bills.append(bill)
        return bill

    def show_bill(self, status):

        for bill in db.bills:
            if status == bill.status:
                print(f"Bike ID: {bill.bike.id}, Client: {bill.client.name}, "
                      f"Date of Rent: {bill.date}, Billing Method: {bill.billing_method}")
                if status == "Closed":
                    print(f"Total income so far: {self.total} EUR")

    def close_bill(self, bike, amount):

        for bill in db.bills:
            if bike == bill.bike:
                bill.status = "Closed"
                bill.price(amount)
                self.total += bill.price(amount)
                bike.status = "AVAILABLE"
            return bill

    def billing_method(self, choice):

        if choice == 1:
            return "Pay per KM", lambda amount: amount * 0.5
        if choice == 2:
            return "Pay per Hour", lambda amount: amount * 7.5
        if choice == 3:
            return "Pay per Day", lambda amount: amount * 45.0


class InputController:

    def int_check(self):
        while True:
            try:
                return int(input("Type an option >> "))
            except ValueError:
                print("Oops!  That was no valid number.  Try again...")
                break
