def monthly_salary(h, p):
    salary = h*p
    rounded_salary = "{: .2f}".format(salary)  # to show even 00 after the comma
    return rounded_salary


if __name__ == '__main__':
    N = int(input("Enter the employee number= "))

    H = float(input("Enter the number of the worked hours = "))

    P = float(input("Enter the amount received per hour = "))

    print(f"EMPLOYEE NUMBER = {N} \nSALARY = U$ {monthly_salary(H,P)}")
