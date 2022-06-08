import employees as employees

from employees import employees


# 1 "Super Car Store" HR Department
# The HR Department of the “Super Car Store” decided to create a file containing information about its employees.
# The intention is to create some programs that can extract some useful information from the dataset.
# The data you can find in the file employees.py as a list of dictionaries.
#
# After gathering the data they gave you the task of implementing some functions to extract the information,
# so you have to implement the following functions.
#
# get_employee_by_name(name) -
# get_total_expenses() -
# get_employees_by_age(age) -
# get_average_age() -
# get_salary_by_name(name) -
# For checking by name use the function/method of string variables called find it will return the position in the string
# where the first occurrence of the word appears or -1 if nothing is found. E.g.


def get_employee_by_name(name):
    [print(f'Are you looking for: {x["employee_name"]}') for x in employees if x["employee_name"].upper().find(name.upper()) != -1]


def get_total_expenses():
    print(sum([x["employee_salary"] for x in employees]))


def get_employees_by_age(age):
    [print(x) for x in employees if x["employee_age"] == age]


def get_average_age():
    print((sum([x["employee_age"] for x in employees])) / len(employees))


def get_salary_by_name(name):
    [print(x["employee_salary"]) for x in employees if x["employee_name"] == name]


if __name__ == '__main__':

    get_employee_by_name("ori")
    #get_total_expenses()
    #get_employees_by_age(61)
    #get_average_age()
    #get_salary_by_name("Doris Wilder")
