from controller import BillingController, BikeController, UserController, InputController
import db


class MainMenu:

    input_controller = InputController()

    def main_menu(self):

        print("1. Rent a bicycle")
        print("2. Return a bicycle")
        print("3. List bicycle")
        print("4. List Bills")
        print("5. Incoming Report")
        print("6. Add Bike")
        print("0. Exit")

        return self.input_controller.int_check()


class SubMenu:

    bike_controller = BikeController()
    billing_controller = BillingController()
    user_controller = UserController()
    input_controller = InputController()

    def manage_user_menu(self):

        while self.user_controller.active_user is None:

            print("Please login or register")
            print("1. Login")
            print("2. Register")
            print("0. Exit")

            return self.input_controller.int_check()

    def login_or_register(self):

        if self.user_controller.active_user is not None:
            return True

        else:
            opt = -1
            while opt != 0:

                opt = self.manage_user_menu()

                if opt not in [1, 2]:
                    print("You cannot rent a bike without an account!")
                elif opt == 1:
                    username = input("Please provide your Username: ")
                    password = input("Please provide your Password: ")
                    if self.user_controller.login_user(username, password):
                        return True
                elif opt == 2:
                    name = input("Please provide your Name: ")
                    username = input("Please choose a Username: ")
                    password = input("Please choose Password: ")
                    self.user_controller.register(name, username, password)
                    return True

    def rent_bike_menu(self):
        if self.login_or_register():
            self.list_bikes_menu()
            user = self.user_controller.active_user
            id = input("Please provide the ID of the bike you wish to rent: ")
            bike = self.bike_controller.get_bike_by_id(id)
            #option = self.billing_menu()
            self.billing_method, self.price = self.billing_controller.billing_method(self.billing_menu())
            print(self.billing_method, self.price)
            self.billing_controller.create_bill(bike, user, self.billing_method, self.price)

    def return_bike_menu(self):

        id = input("Please provide the ID of the bike you wish to return: ")
        for bill in db.bills:
            if bill.bike.id == id:
                res = bill.bike
                print(f"You choose to {bill.billing_method}. How many km, hors, days did you use the bike?")
        amount = self.input_controller.int_check()
        self.billing_controller.close_bill(res, amount)

    def list_bikes_menu(self):
        self.bike_controller.list_bikes()

    def add_bike_menu(self):
        pass

    def billing_menu(self):

        print("Please choose a billing method:")
        print("1. Pay per Kilometer: 0.50 EUR per km")
        print("2. Pay per Hour: 7.50 EUR per hour")
        print("3. Pay per Day: 45.00 EUR per day")
        print("0. Exit")

        opt = -1
        while opt != 0:

            opt = self.input_controller.int_check()

            if opt not in [1, 2, 3]:
                print("That's not a valid choice!")
            else:
                return opt

    def report_menu(self, status):
        self.billing_controller.show_bill(status)
