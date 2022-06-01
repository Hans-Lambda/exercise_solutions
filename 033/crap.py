def user_menu():

    print("Welcome to User Management. Choose an option!")
    print("1. Login")
    print("2. Add Client")
    print("3. Add Partner")
    print("0. Exit")
    option2 = int(input("Type an option >> "))

    option2 = -1

    while option2 != 0:

        option2 = user_menu()

        if option2 == 1:
            users_management.login()
        elif option2 == 2:
            clients_management.add_client()
        elif option2 == 3:
            partners_management.add_partner()


for user in db.users:
    print(user.username, user.password, user.name, user.address, user.client, user.partner)

if user.partner:
    bike = Bike()
    bike.add_bike(bike, user)