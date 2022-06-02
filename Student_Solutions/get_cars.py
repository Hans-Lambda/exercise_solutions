import json
from os import path
car1 = []


def file_open():
    if path.isfile('Cars_test.json') is False:
        raise Exception('File not found')
    with open("Cars_test.json", "r+") as f:
        car1 = json.load(f)
        print(f'The length of records is {len(car1)}')
    return car1


def get_car_by_name(name):
    result = []
    count = 0
    car1 = file_open()
    for car in car1:
        if ((car['Identification']['ID']).lower()).find(name.lower()) > -1:
            result.append(car)
            #print(result, '\n')
            count = 1
    if count != 1:
        print(f'{name} is unavailable')
    print(result, '\n')
    print(f'The number of records is {len(result)}')


def get_car_by_number_of_gears(no_of_gears):
    result = []
    count = 0
    car1 = file_open()
    for car in car1:
        if car["Engine Information"]["Number of Forward Gears"] == no_of_gears:
            result.append(car)
            #print(result, '\n')
            count = 1
    if count != 1:
        print(f'Cars with {no_of_gears} gear(s) is unavailable')
    print(result, '\n')
    print(f'The number of records is {len(result)}')


def get_car_by_manufacturer(manuf_name):
    result = []
    count = 0
    car1 = file_open()
    for car in car1:
        if ((car['Identification']['Make']).lower()).find(manuf_name.lower()) > -1:
            result.append(car)
            #print(result, '\n')
            count = 1
    if count != 1:
        print(f'Cars manufactured by {manuf_name} is unavailable')
    print(result, '\n')
    print(f'The number of records is {len(result)}')


def get_car_by_year(manuf_year):
    result = []
    count = 0
    car1 = file_open()
    for car in car1:
        if car['Identification']['Year'] == manuf_year:
            result.append(car)
            #print(result, '\n')
            count = 1
    if count != 1:
        print(f'Cars manufactured in {manuf_year} is unavailable')
    print(result, '\n')
    print(f'The number of records is {len(result)}')


def get_car_by_average_consumption(des_consumption):
    count = 0
    result = []
    car1 = file_open()
    for car in car1:
        average_consumption = (car['Fuel Information']['City mpg'] + car['Fuel Information']['Highway mpg']) / 2
        if des_consumption >= average_consumption:
            result.append(car)
            # print(result, '\n')
            count = 1
    if count != 1:
        print(f'Cars with an average consumption {des_consumption} is unavailable')
    print(result, '\n')
    print(f'The number of records is {len(result)}')
