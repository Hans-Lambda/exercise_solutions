

users = [
        {
            "name": "Holly",
            "type": "Student",
            "password": "hunter",
            "modules": [
                {
                    "title": "Computer basics",
                    "completed": True
                },
                {
                    "title": "Python basics",
                    "completed": False
                }
            ]
        },
        {
            "name": "Peter",
            "type": "Student",
            "password": "pan",
            "modules": [
                {
                    "title": "Computer basics",
                    "completed": False
                }
            ]
        },
        {
            "name": "Luke",
            "type": "Student",
            "password": "skywalker",
            "modules": [
                {
                    "title": "Computer basics",
                    "completed": True
                }
            ]
        },
        {
            "name": "Janis",
            "type": "Teacher",
            "password": "joplin"
        }
    ]

# Task 1:
# Let's consider the following list of users:


def show_registration(username, password, modulename):

    for user in users:
        if username == user["name"] and password == user["password"] and user["type"] == "Teacher":
            print("You are a teacher.")
            break
        if username == user["name"] and password == user["password"] and user["type"] == "Student":
            for m in user["modules"]:
                if modulename == m["title"]:
                    print(f"You are registered to the module {m['title']}")
        if username == user["name"] and password == user["password"] and user["type"] == "Student":
            for m in user["modules"]:
                if modulename != m["title"]:
                    print(f"You did not register to the module {modulename}")
                break
            break
    if username != user["name"] or password != user["password"]:
        print(f"You did not register to the module {modulename}")


# Task 2
# Now add another function named has_completed_module similar to show_registration with the same input arguments and the following differences:
# This time, the function will do nothing if the user is valid and a teacher.
# It will check if, besides having a particular module in the user's list, the module has the key completed set to True.
# Use the following code to test:


def has_completed_module(username, password, modulename):

    registered = False

    for user in users:
        if username == user["name"] and password == user["password"]:
            if user["type"] == "Student":
                for m in user["modules"]:
                    if modulename == m["title"]:
                        print(f"You are registered to the module {m['title']}")
                        if m["completed"] == True:
                            print(f"You have completed the module {modulename}")
                        if m["completed"] == False:
                            print(f"You did not complete the module {modulename}")
                        registered = True
            if user["type"] == "Teacher":
                print("You are a teacher.")
                registered = True

    #if username != user["name"] or password != user["password"]:
    if not registered:
        print(f"You did not register to the module {modulename}")
        print(f"You did not complete the module {modulename}")


def login():
    username = input("What is your username? ")
    password = input(f"Type the password for {username}: ")
    modulename = input("What module do you want to check? ")
    return username, password, modulename


if __name__ == '__main__':

    username, password, modulename = login()
    #show_registration(username, password, modulename)
    has_completed_module(username, password, modulename)



