from user import UserManager


if __name__ == '__main__':
    user_manager = UserManager()
    user_manager.add_user("Mathias", "SomeStr. 9", "mathias@example.com")

    print(user_manager.get_number_of_users())

    mathias = user_manager.get_user_by_name("Mathias")
    print(mathias.address)

    option = -1
    while option != 0:
        print("Please select an operation")
        print("1. Add user")
        print("2. Remove USer")
        print("3. List Users")
        print("0. Exit")

        option = int(input("Type the option: "))
        if option == 1:
            name = input()
            address = input()
            email = input()
            user_manager.add_user(name, address, email)
        elif option == 2:
            email = input("type the email of the user you want to remove.")
            user_manager.remove_user(email)
        elif option == 3:
            users = user_manager.get_all_users()
            for user in users:
                print(user.name)
