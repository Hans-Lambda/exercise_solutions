def algo_2(a, b, c):

    constant_c = "C is the largest number."

    if a > b:
        if a > c:
            print("A is the largest number.")
        elif c > a:
            print(f"{constant_c}")
        else:
            print("A and C are both the largest number.")
    elif b > a:
        if b > c:
            print("B is the largest number.")
        elif c > b:
            print(f"{constant_c}")
        else:
            print("B and C are both the largest number.")
    elif a == b:
        if a == c:
            print("All numbers are equal.")
        elif a < c:
            print(f"{constant_c}")
        else:
            print("A and B are both the largest number.")


if __name__ == '__main__':

    error_message = "We asked for a number, dumbass!"
    try:
        first = int(input("Please provide a fucking number: "))
    except ValueError:
        print(f"{error_message}")
    try:
        second = int(input("We need another number, you moron: "))
    except ValueError:
        print(f"{error_message}")
    try:
        third = int(input("Moooaaar numbers: "))
    except ValueError:
        print(f"{error_message}")
    algo_2(first, second, third)
