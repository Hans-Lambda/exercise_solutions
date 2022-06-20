from models import Client


class ClientView:

    def __init__(self, client_controller):
        self.client_controller = client_controller

    def main_menu(self):
        print("1. add a Client")
        print("2. remove a Client")
        option = int(input("select an option"))

        if option == 1:
            self.add_client()

    def add_client(self):
        id = int(input("Provide an ID to this client: "))
        name = input("Please give the name of the new client: ")
        email = input("Provide an email to the client: ")
        address = input("PLease type the client email address: ")

        client = Client(id, name, email, address)
        self.client_controller.add_client(client)


class MainView:

    def __init__(self, client_view):
        self.client_view = client_view

    def main_menu(self):
        print("1. manage clients")
        print("2. manage partners")
        print("3. manage bikes")
        option = int(input("Select an option"))

        if option == 1:
            self.client_view.main_menu()
