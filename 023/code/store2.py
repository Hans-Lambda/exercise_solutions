# Write a function that prints out a menu with the option 1. buy, 2. sell, and 0. Exit, the function returns the option
# selected by the user.
# Write 2 functions, one to be executed when the user chooses 1. buy, and another if the user chooses 2. sell.
# These two functions, need to print a submenu to the user with the options available for selling, and for buying.
# The buy and sell functions must return the selected option.

def menu():
    print("1. buy")
    print("2. sell")
    print('0. Exit')

    print("Please select an option...")
    option = int(input())

    return option


def buy():
    print("1. Car")
    print("2. Motorcycle")
    print("3. Stock")
    print("4. Bicycle")

    print("Please select an option...")
    option = int(input())

    return option


def sell():
    print("1. Car")
    print("2. Tv")
    print("3. Sofa")

    print("Please select an option...")
    option = int(input())

    return option


if __name__ == '__main__':
    opt = menu()

    if opt == 1:
        opt2 = buy()
        # code for handling opt2 goes here
    elif opt == 2:
        opt2 = sell()
        # code for handling opt2 goes here
    else:
        exit()

