import sys

# import sys gives exit function

# type main, press tab -> will make main function

# boilerplate code that protects users from accidentally invoking the script when they didn't intend to

# use / to escape characters with special meaning


def menu():
    print("I\'m in the function menu")
    print("1. Check age.")
    print("2. Sell Item")
    print("3. Exit system")
    option = input("Enter your option: ")
    return option


def check_age():
    typed_age = input("Enter your age: ")
    check = int(typed_age) >= 18
    # the comma after string made it accept a boolean and show as string, alternative: ..18?" + str(check))
    print("Is greater than 18?", check)


def sell_item():
    print("Igor is retarded!")


# pass means do nothing

if __name__ == '__main__':
    choice = menu()
    if choice == "1":
        check_age()
    elif choice == "2":
        sell_item()
    elif choice == "3":
        # used to exit program, imported from sys library
        sys.exit("See you soon!")
    else:
        print("You did not select a viable option, you chose: ", choice)
