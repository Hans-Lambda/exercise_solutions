

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

print(f"Name: {user1.name}, Address: {user1.address}, Email: {user1.email}")
print(f"Name: {user2.name}, Address: {user2.address}, Email: {user2.email}")
print(f"Name: {user3.name}, Address: {user3.address}, Email: {user3.email}")

