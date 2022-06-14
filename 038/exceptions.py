import numbers


class AddTwoNumbersError(Exception):
    # input is just passed to the higher level
    pass


def add_two_numbers_0(num1, num2):

    while True:
        try:
            return float(num1) + float(num2)
        except ValueError:
            print("That's not a valid number!")
            break


def add_two_numbers_1(num1, num2):

    result = None
    try:
        result = num1 + num2
    except:
        print("That's not a valid number!")
    return result


def add_two_numbers_2(num1, num2):

    return num1 + num2 if isinstance(num1, numbers.Number) and isinstance(num2, numbers.Number) else None


def add_two_numbers_3(num1, num2):

    try:
        return num1 + num2
    except TypeError:
        print("That's not a valid number!")
    except:
        print("Other Error")


def add_two_numbers_4(num1, num2):

    # num1 in range(20) and num2 in range(20)

    try:
        return num1 + num2
    except ValueError:
        print("Numbers not in acceptable range")
    except TypeError:
        print("That's not a valid number!")
    except:
        print("Other Error")
    finally:
        print("Look at that shitty error handling")


def add_two_numbers_5(num1, num2):

    result = None

    if type(num1) != int:
        raise AddTwoNumbersError(f"{num1} is of wrong type - Expected Integer")
    if type(num2) != int:
        raise AddTwoNumbersError(f"{num2} is of wrong type - Expected Integer")

    return result


if __name__ == '__main__':

    print("****while True loop exception****\n")
    print(add_two_numbers_0(2, "lol"))
    print(add_two_numbers_0(2, 7))

    print("****just try/except****\n")
    print(add_two_numbers_1(2, "lol"))
    print(add_two_numbers_1(2, 7))

    print("****just if/else****\n")
    print(add_two_numbers_2(2, "lol"))
    print(add_two_numbers_2(2, 7))

    print("****TypeError****\n")
    print(add_two_numbers_3(2, "lol"))
    print(add_two_numbers_3(2, 7))

    print("****Finally and multiple error handlers****\n")
    print("\nint and string")
    print(add_two_numbers_4(2, "lol"))
    print("\n22 and 42")
    print(add_two_numbers_4(22, 42))
    print("\n2 and 7")
    print(add_two_numbers_5(2, 7))

    print("****self made error raised****\n")
    print(add_two_numbers_5(2, "lol"))
    print(add_two_numbers_5(2, 7))
