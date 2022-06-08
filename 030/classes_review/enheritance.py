class Shape:

    def __init__(self):
        self.name = "Basic Shape"

    def print(self):
        print(self.name)


class Rectangle(Shape):

    def __init__(self):
        super().__init__()
        self.name = "Rectangle"


if __name__ == '__main__':
    rect1 = Rectangle()
    rect1.print()
