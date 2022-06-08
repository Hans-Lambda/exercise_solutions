class User:

    def __init__(self):

        self.name = None
        self.address = None
        self.email = None
        self.password = None
        self.is_active = False

    def update_data(self, name, address, email):
        self.name = name
        self.address = address
        self.email = email


class UserManager:

    def __init__(self):

        self.users = []

    def add_user(self, name, address, email):
        user = User()
        user.update_data(name, address, email)
        self.users.append(user)

    def remove_user(self, email):

        for user in self.users:
            if user.email == email:
                self.users.remove(user)

    def get_all_users(self):
        return self.users

    def get_number_of_users(self):
        return len(self.users)


user_manager = UserManager()

print(len(user_manager.get_all_users()))            # 0

user_manager.add_user("Franz", "Greifswald", "email@example.com")

print(user_manager.get_number_of_users())           # 1

user_manager.remove_user("email@example.com")

print(user_manager.get_number_of_users())           # 0

user_manager.add_user("Franz", "Greifswald", "email@example.com")
