import math


def triangle_area(b, h):
    return b*h / 2


def circle_area(r):
    return "{: .3f}".format(round(math.pi, 5) * r**2)


def trapezium_area(a, b, c):
    return "{: .3f}".format((a+b)/2*c)


def square_area(b):
    return "{: .3f}".format(b**2)


def rectangle_area(a, b):
    return "{: .3f}".format(a*b)


if __name__ == '__main__':
    A = float(input("Enter the first dimension A = "))
    B = float(input("Enter the second dimension A = "))
    C = float(input("Enter the third dimension A = "))

    print(f"TRIANGLE:{triangle_area(A, C): .2f}")
    print(f"CIRCLE: {circle_area(C)}")
    print(f"trapezium: {trapezium_area(A, B, C)}")
    print(f"SQUARE: {square_area(B)}")
    print(f"RECTANGLE:{rectangle_area(A, B)}")
