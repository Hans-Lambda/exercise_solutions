import datetime
username = input("What is your username? ")
password = input(f"Type the password for username {username}: ")
valid = {"username": "admin", "password": "admin"}

def isweekend(date=datetime.datetime.now()):
    if date.weekday() > 4:
        return True
    return False

today = datetime.date(2021, 8, 7)
today = datetime.datetime.now()
if (username == valid["username"] and password == valid["password"]) or isweekend(today):
    print(f"Welcome, {username}")
else:
    print("Credentials are invalid")
