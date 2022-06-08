import json


def load_users():
    with open('user.json') as file:
        return json.load(file)


def get_subscribers():
    users = load_users()

    result = []
    for user in users:
        if user["is_subscriber"] is True:
            result.append(user)

    return result


def get_active_users():
    users = load_users()

    result = []
    for user in users:
        if user["is_active"] is True:
            result.append(user)

    return result


def get_week_passwords_solution1():
    users = load_users()

    result = []

    for user in users:
        letter = False
        number = False

        for char in user['password']:
            if char.isalpha():
                letter = True
            elif char.isnumeric():
                number = True

        if letter is not True or number is not True:
            result.append(user)

    return result


def get_weak_passwords_divya_solution():
    with open('user.json', 'r') as file:
        data = json.load(file)
    for users in data:
        if (users["password"]).isalpha() or (users["password"]).isnumeric():
            print('\n', users)


def get_weak_passwords_hila_solution():
    users = load_users()
    users_with_weak_passwords = []
    for user in users:
        digit = 0
        letter = 0
        for char in user["password"]:
            if char.isdigit():
                digit += 1
            lower_case = char.lower()
            is_letter = lower_case.islower()
            if is_letter is True:
                letter += 1
        if digit == 0 or letter == 0:
            users_with_weak_passwords.append(user["username"])

    return users_with_weak_passwords


def get_week_passwords_elina_solution():
    users = load_users()
    weekpassusr = []
    for user in users:
        if user['password'].isnumeric() or user['password'].isalpha():
            weekpassusr.append(user)
    return weekpassusr


def get_number_of_users():
    users = load_users()
    return len(users)


def login():
    users = load_users()
    username = input("type your username: ")
    password = input("type your password: ")

    for user in users:
        if user['username'] == username:
            if user['password'] == password and user['is_active'] is True:
                print('success')
                if user['is_subscriber'] is False:
                    print('please subscribe to our service for only 9.999,00 Euros')
                return


def generate_contact_list():
    users = load_users()
    for user in users:
        print(f'{user["username"]} <{user["email"]}>')


def generate_contact_list_peter():
    users = load_users()
    keys = []
    values = []
    for user in users:
        if user["name"]:
            keys.append(user["name"])
        if user["email"]:
            values.append(user["email"])
    results = dict(zip(keys, values))
    return results


def generate_contact_list_peter():
    users = load_users()
    result = dict()

    for user in users:
        result[user["name"]] = user["email"]

    return result


if __name__ == '__main__':
    res = get_subscribers()
    for user in res:
        print(f'{user["username"]} - Subscribed: {user["is_subscriber"]}')
    print("----------")

    res = get_active_users()
    for user in res:
        print(f'{user["username"]} - Active: {user["is_active"]}')

    print("----------")
    res = get_week_passwords_solution1()
    for user in res:
        print(f'{user["username"]} - Password: {user["password"]} Weak')

    print("----------")
    count = get_number_of_users()
    print(f'Number of Users = {count}')

    print("----------")
    login()

    print("----------")
    generate_contact_list()








