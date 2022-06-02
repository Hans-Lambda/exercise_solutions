def is_first_greater(x, y):
    if x > y:
        return True
    else:
        return False


def is_first_greater_v2(x, y):
    return x > y


if __name__ == '__main__':
    print("____v1____")
    print(is_first_greater(3, 4))
    print(is_first_greater(8, 5))
    print("____v2____")
    print(is_first_greater_v2(3, 4))
    print(is_first_greater_v2(8, 5))

    a = int(input("Type number 1: "))
    b = int(input("Type number 2: "))
    print(is_first_greater_v2(a, b))

