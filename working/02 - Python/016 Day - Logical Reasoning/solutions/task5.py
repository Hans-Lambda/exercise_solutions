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

def get_user(username, password):
    for user in users:
        if user["name"] == username and user["password"] == password:
            return user
    return None  # User does not exist --> None -> zero!! zelch!

def is_student(x):
    return x['type'] == 'Student'

def show_offers(username, password):
    user = get_user(username, password)
    # if the user is a student
    # logical operators ---> LEFT to RIGHT
    # TRUE OR FALSE -> TRUE
    # FALSE OR TRUE -> True
    # FALSE OR FALSE -> FALSE
    # not None ->> True --> None -> falsy!!
    if not user or is_student(user): # user -> None
        print("We have great courses to offer you!!")
    else: ## handling of teachers!
        print("You are a teacher, no offers for you!")

username = input("What is your username? ")
password = input(f"Type the password for username {username}: ")
show_offers(username, password)