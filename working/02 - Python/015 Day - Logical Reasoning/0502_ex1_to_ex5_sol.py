import datetime

# Task 1

username = input("What is your username? ")
password = input(f"Type the password for username {username}: ")
valid = {"username": "admin", "password": "admin"}

if username == valid["username"] and password == valid["password"]:
    print(f"Welcome {username}")

if username == valid.get("username", None) and valid.get("password", None):
    print(f"Welcome {username}")


# Task 2


def isweekend(date=datetime.datetime.now()):
    return date.weekday() > 4


if __name__ == '__main__':
    isweekend()
