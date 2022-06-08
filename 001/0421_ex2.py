def salary(number, hours, hourly_pay):

    salary = hours * hourly_pay
    salary_float = "{:.2f}".format(salary)
    print(f"""
        Employee Number = {number}
        Salary = U$ {salary_float}
        """)


if __name__ == '__main__':

    number = int(input("Please type employee number: "))
    hours = float(input("Please type hours: "))
    hourly_pay = float(input("Please type hourly pay: "))
    salary(number, hours, hourly_pay)
