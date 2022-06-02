
username_input = input("What is your username?")
username = "admin"

welcome_message = None

if __name__ == '__main__':

    # welcome_message = "Thank..." if username == username_input
    # if value != zero it is True
    # x = 1 is True

    welcome_message = username == username_input and "Thank you for logging in!"
    print(welcome_message)

    if welcome_message:
        print("Redirect to dashboard")
    else:
        print("Redirect user to Login page")

