import db
import uuid
import datetime as dt


class Bill:

    def __init__(self):

        self.status = None
        self.partner = None
        self.client = None
        self.bike = None
        self.billing_method = None
        self.date = None
        self.id = None
        self.price = None

    def billing_method(self):

        choice = int(input("How would you like to pay? >>>"))
        print("1. By KM - 2.00 EUR per km")
        print("2. By Days - 25.00 EUR per day")
        print("3. By Hour - 5.00 EUR per hour")
        while choice != 0:

            if choice == 1:
                return lambda a: a * 2
            elif choice == 2:
                return lambda b: b * 25
            elif choice == 3:
                return lambda c: c * 5

    def new_bill(self, user, bike, billing_method):

        self.status = "Pending"
        self.partner = bike.partner
        self.client = user
        self.bike = bike
        self.billing_method = billing_method
        self.date = dt.datetime.now()
        self.id = uuid.uuid4()
        self.price = None


class Bike:

    def __init__(self):

        self.age = None
        self.manufacturer = None
        self.type = None
        self.partner = None
        self.status = None
        self.id = str(uuid.uuid4())[:5]

    def add_bike(self, user):

        bike = Bike()
        print("Please provide age, manufacturer and type!")
        bike.age = input("How old is your bike? >>> ")
        bike.manufacturer = input("Which Manufacturer? >>> ")
        bike.type = input("Which Type? >>> ")
        bike.partner = user
        bike.status = "AVAILABLE"

        db.bikes.append(bike)

    def get_bike_by_id(self, bike_id):

        for bike in db.bikes:
            if bike.id == bike_id:
                return bike


class User:

    def __init__(self):

        self.username = None
        self.password = None
        self.name = None
        self.address = None
        self.client = None
        self.partner = None

    def update_data(self, username, password, name, address, client, partner):

        self.username = username
        self.password = password
        self.name = name
        self.address = address
        self.client = client
        self.partner = partner


class UserManagement(User):

    def __init__(self):
        super().__init__()

    def login(self):

        username = input("Username: >>> ")
        password = input("Password: >>> ")

        for user in db.users:
            if username == user.username and password == user.password:
                return user

    def register(self):

        username = input("Choose Username: >>> ")
        password = input("Choose Password: >>> ")
        name = input("Your full name: >>> ")
        address = input("Your address: >>> ")
        rent = input("Do you plan to rent bikes? Y/N >>> ")
        client = True if rent in ["Y", "y", "Yes", "yes"] else False
        rent_out = input("Do you plan to rent out bikes? Y/N >>> ")
        partner = True if rent_out in ["Y", "y", "Yes", "yes"] else False

        new_user = User()
        new_user.update_data(username, password, name, address, client, partner)
        db.users.append(new_user)

        return new_user

    def manage(self):

        print("Login or Register!")
        print("1. Login")
        # maybe add update data
        print("2. Register")
        print("0. Exit")
        option = -1
        option = int(input("Type an option >> "))

        if option == 1:
            return self.login()

        elif option == 2:
            return self.register()


class RentManagement(UserManagement, Bill, Bike):

    def __init__(self):
        super().__init__()

    def rent(self):
        users_management = UserManagement()
        user = users_management.manage()
        list_of_bikes = self.bycicles_list()
        [print(k, v) for k, v in list_of_bikes]
        choice = int(input("Please choose a bike: >>> "))

        for bike in db.bikes:
            if list_of_bikes[choice] == bike:
                self.new_contract(user, bike)

    def bycicles_list(self):
        list_of_bikes = {}
        counter = 1
        for bike in db.bikes:
            list_of_bikes[counter] = [f". Type: {bike.type}, Age: {bike.age}, Manufacturer: {bike.manufacturer}, Status: {bike.status}, ID: {bike.id}"]
            counter += 1
        return list_of_bikes

    def new_contract(self, user, bike):

        bill = Bill()
        billing = bill.billing_method()
        bike.status = "NOT AVAILABLE"
        bill.new_bill(user, bike, billing)
        db.rents.append(bill)
        print(f"You successfully rented a bike!")

    def return_bycicle(self):

        bike_id = input("Please provide the id of the bycycle you like to return: >>>")
        bike = Bike().get_bike_by_id(bike_id)
        bike.status = "AVAILABLE"
        bill_to_close = None
        for bill in db.rents:
            if bike == bill.bike:
                bill_to_close = bill
        amount = int(input("How many km/days/hours: >>> "))
        bill_to_close.price = amount * bill_to_close.billing_method
        print(f"You have to pay {bill_to_close.price}")
        print("Thank you for renting from us!")
        bill_to_close.status = "Closed"

    def bills_list(self):

        bills_list = []
        for bill in db.rents:
            if bill.status == "Pending":
                bills_list.append(bill)

        [print(f"{bill.client.name} rented bike Nr. {bill.bike.id} on {bill.date}") for bill in bills_list]

    def report(self):

        bills_list = []
        total = 0
        for bill in db.rents:
            if bill.status == "Closed":
                bills_list.append(bill)
                total += bill.price

        [print(f"{bill.client.name} rented bike Nr. {bill.bike.id} on {bill.date}. Price: {bill.price}") for bill in bills_list]
        print(f"Total income so far: {total} EUR")
