def dig_2(a):
    return "{:.2f}".format(a)


def salary_adj(salary):

    if 0 <= salary <= 400.00:
        rate = 15
        new_salary = salary * (1 + (rate / 100))
    elif 400.01 <= salary <= 800.00:
        rate = 12
        new_salary = salary * (1 + (rate / 100))
    elif 800.01 <= salary <= 1200.00:
        rate = 10
        new_salary = salary * (1 + (rate / 100))
    elif 1200.01 <= salary <= 2000.00:
        rate = 7
        new_salary = salary * (1 + (rate / 100))
    else:
        rate = 4
        new_salary = salary * (1 + (rate / 100))

    print(f"New Salary: {dig_2(round(new_salary, 2))} Increase: {dig_2(round((new_salary - salary), 2))} Readjustment Rate: {rate} %")


if __name__ == '__main__':
    salary = float(input("Please type the salary: "))
    salary_adj(salary)