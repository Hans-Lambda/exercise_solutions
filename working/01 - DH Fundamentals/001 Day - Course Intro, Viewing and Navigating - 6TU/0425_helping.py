


def calculate_salary(price_per_hour, worked_hours):
    return price_per_hour * worked_hours + 1000


def print_message():
    print("hey")


if __name__ == '__main__':

    print_message()

    employee_number = int(input("Please type employee number: "))
    worked_hours = float(input("Please type worked hours: "))
    price_per_hour = float(input("Please type hourly pay: "))

    salary = calculate_salary(price_per_hour, worked_hours)

    print(f"EMPLOYEE NUMBER = {employee_number}")
    print(f"SALARY = €{salary:.2f}")