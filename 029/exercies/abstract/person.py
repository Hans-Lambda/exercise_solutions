import math


class Math:

    PI = 3.14



    @staticmethod
    def cos(x):
        print("Calculation goes here")

    @staticmethod
    def sqrt(x):
        print("Calculation goes here")


class Date:

    def __init__(self, date):

        self.date = date

    @staticmethod
    def calculate_age(date):
        print("Calculating the date...")


class Person:

    def __init__(self, name, birthday, id_number):

        self.name = name
        self.birthday = birthday
        self.id_number = id_number

    def set_name(self, name):

        self.name = name

    @staticmethod
    # static methods do not need a class object
    # but does not have access to self
    def calculate_age(date_of_birth):
        print("Calculating the age...")


if __name__ == '__main__':

    Person.calculate_age("03.01.1986")
    Date.calculate_age("03.01.1986")

    p1 = Person("Some name", "03.01.1986", "123456789")

    Math.cos(3)
    print(Math.PI)
