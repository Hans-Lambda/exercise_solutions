<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [1 "Super Car Store" HR Department](#1-super-car-store-hr-department)
- [2. The Super Car Store](#2-the-super-car-store)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# 1 "Super Car Store" HR Department

The HR Department of the “Super Car Store” decided to create a file containing information about its employees.
The intention is to create some programs that can extract some useful information from the dataset. The data you can find in the file `employees.py` as a list of dictionaries.

After gathering the data they gave you the task of implementing some functions to extract the information, so you have to implement the following functions.

- `get_employee_by_name(name)`
- `get_total_expenses()`
- `get_employees_by_age(age)`
- `get_average_age()`
- `get_salary_by_name(name)`

For checking by name use the function/method of string variables called
`find` it will return the position in the string where the first occurrence
of the word appears or `-1` if nothing is found. E.g.

```
x = "some text to be used as example"
x.find("example")
24
x.find("not present")
-1
```


# 2. The Super Car Store

The "Super Car Store" is an auto megastore. You can find there
any car you can imagine, its owner cataloged all the cars in a
file and a company developer created a list of dictionaries out of it.
You can find the data in the file `car.py`, and a small subset of the
data in `cars_small`.

The owner intended to have a computer program to help in the
management of the store, allowing him to find some model details easily
for example, or to filter the cars' list based on specific criteria.


You have to create a program with the following functions:

- `def get_car_by_name(name)`
- `def get_car_by_number_of_gears(number_of_gears)`
- `def get_car_by_manufacturer(manufacturer)`
- `def get_car_by_average_comsumption(desired_consumption)`
- `def get_car_by_year(year)`

Every function will return a list of the cars that match the criteria.
For checking by name use the function/method of string variables called
`find` it will return the position in the string where the first occurrence
of the word appears or `-1` if nothing is found. E.g.

```
x = "some text to be used as example"
x.find("example")
24
x.find("not present")
-1
```
