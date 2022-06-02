# https://www.tutorialsteacher.com/python/magic-methods-in-python


class Square:

    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

# other = rigfht side of + operator
# this allows to add objects
    def __add__(self, other):
        return self.area() + other.area()

    def __truediv__(self, other):
        return self.area() / other.area()

    def __gt__(self, other):
        return self.area() > other.area()


if __name__ == '__main__':
    square1 = Square(10)
    square2 = Square(3)

    sum_of_squares = square1 + square2
    div_of_squares = square1 / square2

    print(square1.area())
    print(square2.area())
    print(sum_of_squares)
    print(div_of_squares)
    print(square1 > square2)
