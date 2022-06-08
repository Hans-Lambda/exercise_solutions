def check_pet(owns_a_pet):
    if owns_a_pet == True:
        print("Sorry we do not allow pets")
    else:
        print("You are Welcome")

def print_user_data(name, age, address, weight, owns_a_pet):
    print(name)
    print(age)
    print(address)
    print(weight)
    print(owns_a_pet)


if __name__ == '__main__':
    print('Please type your name:')
    name = input()
    print('Please type your age:')
    age = int(input())
    print('Please type your address:')
    address = input()
    print('Please type your weight:')
    weight = float(input())
    print('Please type if you own a pet (True/False):')
    owns_a_pet = bool(input())

    print_user_data(name, age, address, weight, owns_a_pet)
    check_pet(owns_a_pet)
