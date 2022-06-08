import json

# Task 1
#
# My Loved Users
# Create a program that reads and loads the user.json file as a dictionary in your program.
# Create the following functions:

# 1.1 get_subscribers returns all the users that are subscribers.
# 1.2 get_active_users return all active users
# 1.3 get_week_passwords list all users with week passwords (a strong password must contain both letter and numbers)
# 1.4 get_number_of_users returns the number of users in the system
# 1.5 login asks for the user and password and prints on the screen if the login was successful.
#     Login will also fail if the user is inactive.
#     Login will show a message inviting the user to subscribe if he/she is not yet a subscriber.
# 1.6 generate_contact_list creates a list of users with names and e-mail, e.g.


def load_file():
    with open("/home/user/PycharmProjects/python-course-2022_part1/02 - Python/026 Day - Manipulating Files/"
              "exercise/solution/user.json") as file:
        return json.load(file)


def save_file(data):
    with open("/home/user/PycharmProjects/python-course-2022_part1/02 - Python/026 Day - Manipulating Files/"
              "exercise/solution/user.json", mode="w") as file:
        json.dump(data, file, indent=2)


def get_subscribers():
    data = load_file()
    [print(x) for x in data if x["is_subscriber"]]


def get_active_users():
    data = load_file()
    [print(x) for x in data if x["is_active"]]


def get_week_passwords():
    data = load_file()
    [print(x) for x in data if (x["password"].isalpha() or x["password"].isnumeric())]


def get_number_of_users():
    data = load_file()
    print(len(data))


def login():
    data = load_file()
    username = input("Please provide your username: >>> ")
    password = input("Please provide your password: >>> ")
    for user in data:
        if user["username"] == username and user["password"] == password and user["is_active"]:
            print("Successfully logged in!")
            if not user["is_subscriber"]:
                print("Want to subscribe to get updates?")
# RETURN TO STOP FOR LOOP
            return


def generate_contact_list():
    data = load_file()
    [print(f'Username: {user["name"]}, Email: {user["email"]}') for user in data]


if __name__ == '__main__':
    get_subscribers()
    get_active_users()
    get_week_passwords()
    get_number_of_users()
    login()
    generate_contact_list()
