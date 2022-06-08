import math


def dig_3(a):
    return "{:.3f}".format(a)


def areas(a, b, c):
    triangle = 0.5 * a * c
    radius = math.pi * c**2
    trapezium = 0.5 * (a + b) * c
    square = b**2
    rectangle = a * b

    print(f"""
        TRIANGLE: {dig_3(triangle)}
        CIRCLE: {dig_3(radius)}
        TRAPEZIUM: {dig_3(trapezium)}
        SQUARE: {dig_3(square)}
        RECTANGLE: {dig_3(rectangle)}
        """)



if __name__ == '__main__':
    x = float(input("Please type length of side A: "))
    y = float(input("Please type length of side B: "))
    z = float(input("Please type length of side C: "))
    areas(x, y, z)