

class User:

    def __init__(self):

        self.name = None
        self.address = None
        self.email = None
        self.password = None

    def update_data(self, name, address, email):
        self.name = name
        self.address = address
        self.email = email


user1 = User()
user2 = User()
user3 = User()

user1.name = "Uhrensohn"
user1.address = "Uhrensohnstraße 69"
user1.email = "fuckoff@email.fuck"
user1.password = "suckmydick"

user2.name = "Mathias"
user3.name = "Billy"
user2.update_data("Lama", "Address", "example@email.com")

list_of_users = [user1, user2, user3]

for user in list_of_users:
    print(f"Name: {user.name}, Address: {user.address}, Email: {user.email}")
