# Task 1

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


def get_user(username, password):
    """Return the first user matching username and password."""
    return next((u for u in users
                 if u["name"] == username and u["password"] == password)
                , None)


def module_registered(user, modulename):
    """Return the context of a registered module for a particular user."""
    return next((module for module in user['modules']
                 if module["title"] == modulename)
                , None)


def is_student(user):
    """Return True if the user is a student."""
    return user and user["type"] == "Student"


def show_registration(username, password, modulename):
    """Print if the user is registered to a module or is a teacher."""
    user = get_user(username, password)
    if is_student(user) and module_registered(user, modulename):
        print(f"You are registered to the module {modulename}.")
    elif not user or is_student(user):
        print(f"You did not register to the module {modulename}.")
    else:
        print(f"You are a teacher.")


# # Test cases
# username = input("What is your username? ")
# password = input(f"Type the password for username {username}: ")
# modulename = input("What module do you want to check? ")
# show_registration(username, password, modulename)


# Task 2

def has_completed_module(username, password, modulename):
    """Return True if the user has completed a specific module."""
    user = get_user(username, password)
    if user and is_student(user):
        module = module_registered(user, modulename)
        if module and module["completed"]:
            print(f"You have completed the module {modulename}.")
            return
    if not user or is_student(user):
        print(f"You did not complete the module {modulename}.")


# # Test cases
# username = input("What is your username? ")
# password = input(f"Type the password for username {username}: ")
# modulename = input("What module do you want to check? ")
# show_registration(username, password, modulename)
# has_completed_module(username, password, modulename)


# Task 3

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
    """Return True if the user is eligible for registration on the modulename."""
    user = get_user(username, password)
    module = get_module(modulename)
    return (is_anonymous(user) and has_no_requirement(module)
            or is_student(user) and meets_requirement(user, module))


def get_module(modulename):
    """Return the first module matching modulename."""
    return next(
        (module for module in modules
         if module["name"] == modulename)
        , None)


def is_anonymous(user):
    """Return True if the user is anonymous."""
    return not user


def has_no_requirement(module):
    """Return true if the module has no requirement."""
    return module and "requirement" not in module


def meets_requirement(user, module):
    """Return True if the user meets the module's requirement."""
    return module and not module_registered(user, module["name"]) and (
        has_no_requirement(module)
        or module_completed(user, module["requirement"])
    )


def module_completed(user, modulename):
    """Return the context of a completed module for a particular user."""
    return next(
        (m for m in user["modules"]
         if m["title"] == modulename and m["completed"])
        , None)


# # Test cases
username = input("What is your username? ")
password = input(f"Type the password for username {username}: ")
modulename = input("What module do you want to check? ")
show_registration(username, password, modulename)
has_completed_module(username, password, modulename)
if may_enroll(username, password, modulename):
    print(f"You may register to the module {modulename}.")
else:
    print(f"You may not register to the module {modulename}.")
