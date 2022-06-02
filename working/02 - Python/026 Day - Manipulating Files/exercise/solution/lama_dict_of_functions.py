import json

with open("user.json") as file:
    users = json.load(file)


def upload(some_object, some_file):
    with open(some_file, "w") as f:
        json.dump(some_object, f, indent=2)

"""
def has_only_numbers(inputString):
    return all(char.isdigit() for char in inputString)
def has_some_numbers(inputString):
    return any(char.isdigit() for char in inputString)"""


def get_user(name, password):
    return [user for user in users if user["username"] == name and user["password"] == password]


def get_subscribers():
    # return [user for user in users if user["is_subscriber"] is True]
    [print("Subscribed user:\n", user) for user in users if user["is_subscriber"] is True]


def get_active_users():
    # return [user for user in users if user["is_active"] is True]
    [print("Active user: ", user) for user in users if user["is_active"] is True]


def get_weak_passwords():
    # return [user for user in users if has_only_numbers(user["password"]) or not has_some_numbers(user["password"])]
    # return [user for user in users if (user["password"].isalpha() or user["password"].isnumeric())]
    [print("user with weak password:\n", user) for user in users if (user["password"].isalpha() or user["password"].isnumeric())] # from Franz


def get_number_of_users():
    return len(users)


def login():
    user_input = input("Enter the username: ")
    password_input = input("Enter the password: ")
    user = get_user(user_input, password_input)
    print("login failed! please check your data or subscribe to our webservice") if not user or user[0][
        "is_subscriber"] is False else print("welcome!")


def generate_contact_list():
    with open('contact_list.txt', 'w') as f:
        [print(user["username"], " <", user["email"], ">", file=f) for user in users]

"""
read:
https://softwareengineering.stackexchange.com/questions/182093/why-store-a-function-inside-a-python-dictionary
https://stackoverflow.com/questions/9168340/using-a-dictionary-to-select-function-to-execute
"""

def menu():
    l = ["get_subscribers", "get_active_users", "get_weak_passwords", "get_number_of_users", "login",
         "generate_contact_list", "Exit"]
    print("What do you want to do? select an action of the list:")
    [print(i, ". ", action) for i, action in enumerate(l, 1)]
    option = int(input("Type the corresponding number here: "))
    functions = {1: get_subscribers, 2: get_active_users, 3: get_weak_passwords, 4: get_number_of_users,
                 5: login, 6: generate_contact_list, 7: exit}

    # while True:

    while option not in range(1, 8):  # check range
        print("Option does not exist. Try again!")
        option = int(input("Type the corresponding number here: "))

    function = functions[option]
    return function()


if __name__ == '__main__':

    menu()
