def largest_from_three(a, b, c):
    if a > b:
        if a > c:
            print("A is the largest number.")
        else:
            print("C is the largest number.")
    else:
        if b > c:
            print("B is the largest number.")
        else:
            print("C is the largest number.")


if __name__ == '__main__':
    largest_from_three(-11, -5, 9)
