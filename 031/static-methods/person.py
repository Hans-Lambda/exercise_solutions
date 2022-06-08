class Math:

    PI = 3.14

    @staticmethod
    def cos(x):
        print("calculations goes here")

    @staticmethod
    def sqrt(x):
        print("calculations goes here")


class Date:

    def __int__(self, date):
        self.date = date

    @staticmethod
    def calculate_age(date):
        print("calculating the age...")


class Person:

    def __init__(self, name, birthday, id_number):
        self.name = name
        self.birthday = birthday
        self.id_number = id_number

    def set_name(self, name):
        self.name = name

    @staticmethod
    def calculate_age(date_of_birth):
        print("Calculation goes here...")
        # TOD implement the calculation


if __name__ == '__main__':
    Person.calculate_age("22.12.1982")
    Date.calculate_age('22.12.1982')

    p1 = Person("Somename", "22-12-1982", "21932130921")
    p1.set_name("Some Other Name")

    Math.cos(3)
    print(Math.PI)


