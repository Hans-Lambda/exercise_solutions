import math

from check import print_rectangle_properties


class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return self.width * 2 + self.height * 2

    def get_diagonal(self):
        return math.sqrt(self.width**2 + self.height**2)

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height


def main():
    rectangle1 = Rectangle(3.5, 5.2)
    rectangle2 = Rectangle(4, 4)

    print_rectangle_properties(rectangle1)
    print_rectangle_properties(rectangle2)


if __name__ == "__main__":
    main()
