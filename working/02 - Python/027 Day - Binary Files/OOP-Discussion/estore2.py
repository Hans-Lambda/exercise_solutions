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
user3.update_data("Peter", "someaddress 10", "someemail@something.com")

list_of_users = [user1, user2, user3]

for user in list_of_users:
    print(f'Name: {user.name}, Address: {user.address}, email: {user.email}')
