import math
from abc import ABC, abstractmethod


class Shape(ABC):

    def __init__(self):
        self.name = ""

    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass

    def print(self):
        print(f'Shape is: {self.name}, its area is {self.calculate_area()} and '
              f'its perimeter is {self.calculate_perimeter()}')


class Rectangle(Shape):

    def __init__(self, width, height):
        super().__init__()
        self.name = "Rectangle"
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return self.width*2 + self.height*2


class Triangle(Shape):

    def __init__(self, side1, side2, side3):
        super().__init__()
        self.name = "Triangle"
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        if self.check_sides() is True:
            print("Valid Triangle!")
        else:
            print("Error: Invalid Triangle!")

    def check_sides(self):
        if (self.side1 + self.side2 > self.side3 and
                self.side1 + self.side3 > self.side2 and
                self.side2 + self.side3 > self.side1 and
                self.side3 > abs(self.side1 - self.side2)):
            return True
        return False

    def calculate_area(self):
        s_p = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(s_p * (s_p - self.side1) * (s_p - self.side2) * (s_p - self.side3))

    def calculate_perimeter(self):
        return self.side1 + self.side2 + self.side3


class Pentagon(Shape):

    def __init__(self, side):
        super().__init__()
        self.name = "Pentagon"
        self.side = side

    def calculate_area(self):
        return (math.sqrt(5 * (5 + 2 * math.sqrt(5))) * pow(self.side, 2)) / 4.0

    def calculate_perimeter(self):
        return 5 * self.side


class Circle(Shape):

    def __init__(self, radius):
        super().__init__()
        self.name = "Circle"
        self.radius = radius

    def calculate_area(self):
        return math.pi * (self.radius**2)

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius
