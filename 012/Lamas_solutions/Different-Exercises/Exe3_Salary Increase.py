# Readjustment Rate:
def re_rate(s):
    if 0 <= s <= 400.00:
        r = 0.15
    elif 400.01 <= s <= 800.0:
        r = 0.12
    elif 800.01 <= s <= 1200.00:
        r = 0.10
    elif 1200.01 <= s <= 2000.00:
        r = 0.07
    else:
        r = 0.04
    return r


# Increase
def increase(s):
    if 0 <= s <= 400.00:
        r = 0.15
    elif 400.01 <= s <= 800.0:
        r = 0.12
    elif 800.01 <= s <= 1200.00:
        r = 0.10
    elif 1200.01 <= s <= 2000.00:
        r = 0.07
    else:
        r = 0.04

    inc = s * r
    return "{: .2f}".format(inc)


# new salary
def new_salary(s):
    if 0 <= s <= 400.00:
        r = 0.15
    elif 400.01 <= s <= 800.0:
        r = 0.12
    elif 800.01 <= s <= 1200.00:
        r = 0.10
    elif 1200.01 <= s <= 2000.00:
        r = 0.07
    else:
        r = 0.04

    inc = s * r
    return "{: .2f}".format(s + inc)


if __name__ == '__main__':
    salary = float(input("Enter the Salary = "))

    print(f"New Salary: {new_salary(salary)} Increase: {increase(salary)} Readjustment Rate: {re_rate(salary)} %")
