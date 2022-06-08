def largest_among_two(a, b):
    if a > b:
        print("a is greater than b")
    else:
        print("b is greater than a")


if __name__ == '__main__':
    first = int(input())
    second = int(input())
    largest_among_two(first, second)
