def is_first_greater(x, y):
    if x > y:
        return True
    else:
        return False


def is_first_greater_v2(x, y):
    return x > y


if __name__ == '__main__':
    print("-------- is_first_greater")
    print(is_first_greater(3, 4))
    print(is_first_greater(8, 5))
    print("-------- is_first_greater_v2")
    print(is_first_greater_v2(3, 4))
    print(is_first_greater_v2(8, 5))
    print("-------- with inputs")
    a = int(input())
    b = int(input())
    print(is_first_greater(a, b))



