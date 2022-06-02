import math


class Rectangle:

    def __init__(self, width, height):
        self.name = "Rectangle"
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return self.width*2 + self.height*2

    def print(self):
        print(f'Shape is: {self.name}, its area is {self.calculate_area()} and its perimeter is {self.calculate_perimeter()}')


class Triangle:

    def __init__(self,  side1, side2, side3):
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

    def print(self):
        print(f'Shape is: {self.name}, its area is {self.calculate_area()} and its perimeter is {self.calculate_perimeter()}')


class Pentagon:

    def __init__(self, side):
        self.name = "Pentagon"
        self.side = side

    def calculate_area(self):
        return (math.sqrt(5 * (5 + 2 * math.sqrt(5))) * pow(self.side, 2)) / 4.0

    def calculate_perimeter(self):
        return 5 * self.side

    def print(self):
        print(f'Shape is: {self.name}, its area is {self.calculate_area()} and its perimeter is {self.calculate_perimeter()}')


class Circle:

    def __init__(self, radius):
        self.name = "Circle"
        self.radius = radius

    def calculate_area(self):
        return math.pi * (self.radius**2)

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius

    def print(self):
        print(f'Shape is: {self.name}, its area is {self.calculate_area()} and its perimeter is {self.calculate_perimeter()}')
