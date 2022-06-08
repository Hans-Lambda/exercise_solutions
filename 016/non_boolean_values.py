# username_input = input("What is your username?")
username = "admin"

welcome_message = None  # Optional!

if __name__ == '__main__':
    # welcome_message = username == username_input and "Thank you for logging in"
    # welcome_message = False and "Thank you for logging in"
    # print(welcome_message)
    # if welcome_message:
    #     print("redirect to a dashboard")
    # else:
    #     print("redirect this user to login page")
    # if username_input == username:
    #     welcome_message = "Thank you for logging in!"
    # else:
    #     welcome_message = "Try again!"
    #
    # # Confirm that it was set with a value
    # print(welcome_message)
    user = input("hello: ")
    # "" ==> falsey !
    print(type(user), user)
