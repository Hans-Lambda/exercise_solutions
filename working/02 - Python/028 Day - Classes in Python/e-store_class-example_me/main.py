from user import UserManager

if __name__ == '__main__':
    user_manager = UserManager()
    user_manager.add_user("Franz", "Fuckstreet 69", "nicedick@me.com")

    print(user_manager.get_number_of_users())

    franz = user_manager.get_user_by_name("Franz")
    print(franz.address)


    option = -1
    while option != 0:
        print("Please select an operation")
        print("1. Add user")
        print("2. Remove user")
        print("3. List users")
        print("4. Start shopping")
        print("0. Exit")

        option = int(input("Type the option: >>> "))
        if option == 1:
            name = input("Name: ")
            address = input("Address: ")
            email = input("Email: ")
            user_manager.add_user(name, address, email)
        elif option == 2:
            email = input("Type the Email of the user to be removed: ")
            user_manager.remove_user(email)
        elif option == 3:
            users = user_manager.get_all_users()
            for user in users:
                print(f"\nName: {user.name}\nAddress: {user.address}\nEmail: {user.email}\n")
