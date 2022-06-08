import sys


def is_logged_in(username, password):

    # conditional logic
    if username == "admin" and password == "123456":
        print("You have successfully logged in!")
    if username == "Hans_Lambda" and password == "FuckPutin":
        print("You have successfully logged in!")
    else:
        print("Try again!")
        login()
    sys.exit()

def login():
    username = input("Please type your username: ")
    password = input("Please type your password: ")
    is_logged_in(username, password)


if __name__ == '__main__':
    login()
