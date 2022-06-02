username = input("What is your username? ")
password = input(f"Type the password for username {username}: ")

# list -> use numbers!!!! list[0] -> zeroth item in a list, list[1] you get the first
# diction -> use keys (strings) dictionary["key"]

# Data structure - Dictionary (little "database")
valid = {"username": "admin", "password": "admin"}
# search -- e.g. for loop! (very slow)
# Your code here
# annoying thing -> more than two ways (traditional classical way of accessing dictionary values)
# if username == valid["username"] and password == valid["password"]:
#     print(f"Welcome, {username}")
# else:
#     print("Credentials are invalid")

# another way of getting values out of a dictionary
# if username == valid.get("username", None) and password == valid.get("password", None):
#
#     print(f"Welcome, {username}")
# else:
#     print("Credentials are invalid")

# don't stress (another way of doing the same thing)
# while username != valid.get("username", None) and password != valid.get("password", None):
#     username = input("What is your username? ")
#     password = input(f"Type the password for username {username}: ")
# else:
#     print(f"Welcome, {username}")
