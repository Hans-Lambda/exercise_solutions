class Person:

    def __init__(self, name, address, birthday, gender, height, weight, color, marital_status, country):
        self.name = name
        self.address = address
        self.birthday = birthday
        self.gender = gender
        self.height = height
        self.weight = weight
        self.color = color
        self.marital_status = marital_status
        self.country = country
        self.has_passport = False

    def register_in_a_country(self, country_name):
        self.country = country_name

    def issue_passport(self):
        self.has_passport = True

    def get_married(self):
        self.marital_status = "married"


class Employee(Person):

    def __init__(self, name, address, birthday, gender, height, weight, color, marital_status, country, position):
        super().__init__(name, address, birthday, gender, height, weight, color, marital_status, country)
        self.salary = 1000
        self.position = position
        self.address = "someaddress"

    def increase_salary(self, amount):
        self.salary += amount

    def print(self):
        print(self.name)


class Customer(Person):

    def __init__(self, name, address, birthday, gender, height, weight, color, marital_status, country):
        super().__init__(name, address, birthday, gender, height, weight, color, marital_status, country)
        self.customer_number = None

    def set_customer_number(self, number):
        self.customer_number = number


if __name__ == '__main__':

    customer1 = Customer("Mathias", "SomeStr 5", "129813", "Male", 180, 82, "Brown/Black", "Single", "Germany")
    customer1.issue_passport()

    employee1 = Employee("Someonelese", "SomeStr 5", "129813", "Male", 180, 82, "Brown/Black", "Single", "Germany",
                         "manager")
    employee1.get_married()
