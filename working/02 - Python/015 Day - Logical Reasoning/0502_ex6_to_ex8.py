

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
# Using the concepts, and some code from the previous exercises, define a function named show_registration that checks
# if a user is registered to a specific module.
# The function will accept three input arguments:
# username. String
# password. String
# modulename. String
# The function may print any of the following messages:
# You are registered to the module {modulename}. It will print this message if the user is a student and in his modules
# key has a module with a title equal to the argument modulename
# You did not register to the module {modulename} It will print this message if the user is anonymous or is a student
# and in his modules key DOES NOT have a module with the given title.
# You are a teacher It will print this message if the username is a teacher.


def show_registration(username, password, modulename):

    # this is shit, see "has_completed_module" for better approach

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
# Now add another function named has_completed_module similar to show_registration with the same input arguments and the
# following differences:
# This time, the function will do nothing if the user is valid and a teacher.
# It will check if, besides having a particular module in the user's list, the module has the key completed set to True.
# Use the following code to test:


def has_completed_module(username, password, modulename):

    registered = False

    for user in users:
        if username == user["name"] and password == user["password"]:
            if user["type"] == "Student":
                for module in user["modules"]:
                    if modulename == module["title"]:
                        print(f"You are registered to the module {module['title']}")
                        if module["completed"]:
                            print(f"You have completed the module {modulename}")
                        else:
                            print(f"You did not complete the module {modulename}")
                        registered = True
            if user["type"] == "Teacher":
                print("You are a teacher.")
                registered = True

    #if username != user["name"] or password != user["password"]:
    if not registered:
        print(f"You did not register to the module {modulename}")
        print(f"You did not complete the module {modulename}")


# Task 3
# Now we are given this list of modules:
# Add a new function named may_enroll with three input parameters:
# username. String
# password. String
# modulename. String
# This function should return True in the following cases:
# The user is anonymous and the module has no requirement (they can always register).
# The user is a student and:
# The user is not already registered to that module.
# The module has no requirement or it has one and the user meets the requirement (is also registered to the requirement
# and its completed flag is set to True).
# In any other case, the function should return False.

modules = [
    {
        "name": "Computer basics"
    },
    {
        "name": "Python basics",
        "requirement": "Computer basics"
    },
    {
        "name": "Django",
        "requirement": "Python basics"
    }
]


def may_enroll(username, password, modulename):
    registered = False

    for user in users:
        if username == user["name"] and password == user["password"]:
            if user["type"] == "Student":
                for mod in user["modules"]:
                    if modulename == mod["title"]:
                        print(f"You are registered to the module {mod['title']}")
                        if mod["completed"]:
                            print(f"You have completed the module {modulename}")
                            print(f"You may not register to the module {modulename}.")
                        else:
                            print(f"You did not complete the module {modulename}")
                            print(f"You may not register to the module {modulename}.")
                        registered = True
            if user["type"] == "Teacher":
                print("You are a teacher.")
                print(f"You may not register to the module {modulename}.")
                registered = True

    # if username != user["name"] or password != user["password"]:
    if not registered:

        offered = False

        print(f"You did not register to the module {modulename}")
        print(f"You did not complete the module {modulename}")
        for module in modules:
            if modulename == module["name"] and len(module) == 1:
                print(f"You may register to the {modulename}.")
                offered = True
            if modulename == module["name"] and len(module) > 1:
                offered = True
                for user in users:
                    if username != user["name"] or password != user["password"]:
                        print(f"You may not register to the module {modulename}.")
                        break
                    if username == user["name"] and password == user["password"]:
                        if user["type"] == "Student":
                            for mod in user["modules"]:
                                if module["requirement"] == mod["title"]:
                                    if mod["completed"]:
                                        print(f"You may register to the {modulename}.")
                                    else:
                                        print(f"You may not register to the module {modulename}.")
        if offered == False:
            print(f"You may not register to the module {modulename}.")


def login():
    username = input("What is your username? ")
    password = input(f"Type the password for {username}: ")
    modulename = input("What module do you want to check? ")
    return username, password, modulename


if __name__ == '__main__':

    username, password, modulename = login()
    #show_registration(username, password, modulename)
    #has_completed_module(username, password, modulename)
    may_enroll(username, password, modulename)



