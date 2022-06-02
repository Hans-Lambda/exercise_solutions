from employees import employees


def get_employee_by_name(name_to_search):
    for employee in employees:
        if employee["employee_name"] == name_to_search:
            print("something")


if __name__ == '__main__':
    for employee in employees:
        print(employee["employee_name"])

    get_employee_by_name("Mathias")
