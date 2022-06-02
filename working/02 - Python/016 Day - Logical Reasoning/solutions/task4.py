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

def get_user(username, password):
    for user in users:
        if user["name"] == username and user["password"] == password:
            return user
    return None  # User does not exist --> None -> zero!! zelch!

def get_user_version2(username, password):
    return next((u for u in users
                 if u["name"] == username and u["password"] == password), None)


username = input("What is your username? ")
password = input(f"Type the password for username {username}: ")
# user = get_user(username, password)
user = get_user_version2(username, password)
# Rest of your code here
if not user:
    print("An error occurred. You are not authorized.")