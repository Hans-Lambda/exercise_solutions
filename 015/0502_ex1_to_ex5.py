import datetime

# Task 1
# Validate the input credentials of a user. You should print the message Welcome, {username}!
# if the credentials are valid and the message Credentials are invalid if they are not.


def login():
    username = input("What is your username? ")
    password = input(f"Type the password for username {username}: ")
    valid = {"username": username, "password": password}
    if username == valid.get("username", None) and password == valid.get("password", None):
        print(f"Welcome {username}")


# Task 2
# Define a function named isweekend that accepts a parameter named date of type Datetime (with a default value of datetime.datetime.now()).
# This function will serve as a logical expression and will return True if the day of the week in the date is either Saturday or Sunday.
# It will return False in any other case.
# You can actually do this in many ways, but in this exercise you are required to use the OR operator.


def is_weekend(date):
    return date.weekday() > 4


# Task 3
# We now want a version of the first task, that will implement an "open doors" policy on the weekends.
# So, if the user credentials are valid, or the date is on the weekend, the conditional should evaluate to True and greet the user.
# Use a single logical expression.
# Reuse the isweekend(<Datetime>) function from before.


def open_doors(date=datetime.datetime.now()):
    username = input("What is your username? ")
    password = input(f"Type the password for username {username}: ")
    #today = datetime.date(2021, 8, 7)
    valid = {"username": "admin", "password": "admin"}
    if is_weekend(date) or (username == valid.get("username") and password == valid.get("password")):
        print(f"Welcome {username}")
    else:
        print("Credentials are invalid")


# Task 4
# Now define a function named get_user with the input arguments username and password, both as a String.
# There is a global variable named users as a list of dictionaries:


def get_user(username, password):

    users = [
        {
            "name": "Holly",
            "password": "hunter"
        },
        {
            "name": "Peter",
            "password": "pan"
        },
        {
            "name": "Janis",
            "password": "joplin"
        }
    ]

    for user in users:
        if username == user["name"] and password == user["password"]:
        #if username == (list(user.values())[0]) and password == (list(user.values())[1]):
            print(list(user.items()))
            break
        else:
            print("An error occurred. You are not authorized.")
            return None


# Task 5
# Replace the previous list of users with the following one:


def show_offers(username, password):
    users = [
        {
            "name": "Holly",
            "type": "Student",
            "password": "hunter"
        },
        {
            "name": "Peter",
            "type": "Student",
            "password": "pan"
        },
        {
            "name": "Janis",
            "type": "Teacher",
            "password": "joplin"
        }
    ]

    username = input("What is your username? ")
    password = input(f"Type the password for username {username}: ")

    for user in users:
        if username == user["name"] and password == user["password"] and user["type"] == "Student":
        #if username == (list(user.values())[0]) and password == (list(user.values())[2]) and (list(user.values())[1]) == "Student":
            print("We have great courses to offer you!")


if __name__ == '__main__':

    #login()
    #is_weekend(datetime.date(2021, 8, 7))
    #open_doors(datetime.date(2022, 5, 2))
    #get_user("Holly", "hunter")
    #show_offers("Holly", "hunter")
