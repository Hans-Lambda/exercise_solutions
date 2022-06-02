def calculate_salary(price_per_hour, worked_hours):
    return price_per_hour * worked_hours + 1000


def print_message():
    print("hey")


if __name__ == '__main__':
    employee_number = int(input())
    worked_hours = float(input())
    price_per_hour = float(input())

    salary = calculate_salary(price_per_hours, worked_hours)
    print_message()


    print(f"EMPLOYEE NUMBER = {employee_number}")
    print(f"SALARY = ${salary:.2f}")
