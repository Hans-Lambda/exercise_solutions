def largest_from_three(a, b, c):
    if a > b:
        if a > c:
            print("a is the largest")
        else:
            print("c is the largest")
    else:
        if b > c:
            print("b is the largest")
        else:
            print("c is the largest")


if __name__ == '__main__':
    first = int(input())
    second = int(input())
    third = int(input())
    largest_from_three(first, second, third)
