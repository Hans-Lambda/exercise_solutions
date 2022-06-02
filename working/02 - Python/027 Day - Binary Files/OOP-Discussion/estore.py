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

user1.update_data("Mathias", "SomeStr. 9", "mathias@example.com")
user2.update_data("Billy", "Somewhere 6", "billy@example.com")
user3.name = "Peter"
user3.address = "someaddress 10"
user3.email = "someemail@something.com"

print(f'Name: {user1.name}, Address: {user1.address}, email: {user1.email}')
print(f'Name: {user2.name}, Address: {user2.address}, email: {user2.email}')
print(f'Name: {user3.name}, Address: {user3.address}, email: {user3.email}')
