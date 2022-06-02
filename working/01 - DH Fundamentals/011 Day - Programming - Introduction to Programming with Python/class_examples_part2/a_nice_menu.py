import sys


def menu():
    print('IM in the function menu')
    print('1. Check age.')
    print('2. Sell Item')
    print('3. exit')
    option = input()
    return option


def check_age():
    print("What's your age? ")
    typed_age = input()
    check = int(typed_age) >= 23
    print("Is greater than 18? " + str(check))


def sell_item():
    print("Item sold!")


if __name__ == '__main__':
    choice = menu()
    if choice == '1':
        check_age()
    elif choice == '2':
        sell_item()
    elif choice == '3':
        sys.exit()
    else:
        print('You did not selected 1, you selected' + str(choice))
