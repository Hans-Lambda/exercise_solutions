import sys
import json
from os import path

import get_cars


def insert_car():
    return get_dimensions(), get_engine_information(), get_fuel_information(), get_identification()


def get_dimensions():
    height = int(input('enter the car dimensions_height'))
    length = int(input('enter the car dimensions_length'))
    width = int(input('enter the car dimension_width'))
    Dimensions_Values["Height"] = height
    Dimensions_Values["Length"] = length
    Dimensions_Values["Width"] = width
    print(Dimensions_Values)
    Dimensions["Dimensions"] = Dimensions_Values
    return Dimensions


def get_engine_information():
    driveline = input('Enter the drive line')
    engine_type = input('Enter the engine type')
    print('Is hybrid (Yes / No)', end='')
    hybrid_value = input()
    if hybrid_value.lower() == 'yes':
        hybrid = 'True'
    else:
        hybrid = 'False'
    number_of_forward_gears = int(input('Enter the number of forward gears'))
    transmission = input('Enter the transmission')
    horsepower = input('Enter the horsepower')
    torque = input('Enter the torque')
    Engine_Values["Driveline"] = driveline
    Engine_Values["Engine Type"] = engine_type
    Engine_Values["Hybrid"] = hybrid
    Engine_Values["Number of Forward Gears"] = number_of_forward_gears
    Engine_Values["Transmission"] = transmission
    Engine_Statistics_Values["Horsepower"] = horsepower
    Engine_Statistics_Values["Torque"] = torque
    Engine_Statistics["Engine Statistics"] = Engine_Statistics_Values
    Engine_Values.update(Engine_Statistics)
    #print(Engine_Values)
    Engine_Information["Engine_Information"] = Engine_Values
    return Engine_Information


def get_fuel_information():
    city_mpg = float(input('enter the city mpg'))
    fuel_type = input('enter the fuel type')
    highway_mpg = float(input('enter the highway mpg'))
    Fuel_Information_Values["City mpg"] = city_mpg
    Fuel_Information_Values["Fuel Type"] = fuel_type
    Fuel_Information_Values["Highway mpg"] = highway_mpg
    #print(Fuel_Information_Values)
    Fuel_Information["Fuel_Information"] = Fuel_Information_Values
    return Fuel_Information


def get_identification():
    classification = input('enter the classification')
    id_name = input('enter the ID')
    make = input('enter the manufacturer')
    model_year = input('enter the model year')
    year_value = input('enter the year')
    Identification_Values["Classification"] = classification
    Identification_Values["ID"] = id_name
    Identification_Values["Make"] = make
    Identification_Values["Model Year"] = model_year
    Identification_Values["Year"] = year_value
    #print(Identification_Values)
    Identification["Identification"] = Identification_Values
    return Identification


def update_car():
    id_name = input('Enter the Id of the car to be updated')
    new_id = input('Enter the new ID')
    if path.isfile('Cars_test.json') is False:
        raise Exception('File not found')
    with open("Cars_test.json", "r+") as f:
        car1 = json.load(f)
        for car in car1:
            if ((car['Identification']['ID']).lower()).find(id_name.lower()) > -1:
                car["Identification"]["ID"] = new_id
                # print(car1)
                with open("Cars_test.json", 'w') as fw:
                    json.dump(car1, fw, indent=4, separators=(',', ': '))
                print('Successfully updated to Cars_test_Json')
                break
                #print("Successfully updated")
            #else:
                #print('ID not found !!!')
        #car1.append(car_values)


def get_option():
    option = input('1. Get a car by name\n2. Get cars by the number of gears\n3.Get cars by Manufacture\n4.Get a car '
                   'by the year\n5.Get a car by average consumption \n 6.Insert new car \n7. Update a car\n 0. Exit\n '
                   'Enter the option')
    if option == '1':
        car_name = input('Enter the car name')
        get_cars.get_car_by_name(car_name)
    elif option == '2':
        number_of_gears = int(input('Enter the number of gears'))
        get_cars.get_car_by_number_of_gears(number_of_gears)
    elif option == '3':
        manufacturer = input('Enter the manufacturer')
        get_cars.get_car_by_manufacturer(manufacturer)
    elif option == '4':
        year = int(input('Enter the year'))
        get_cars.get_car_by_year(year)
    elif option == '5':
        desired_consumption = float(input('Enter the desired consumption'))
        get_cars.get_car_by_average_consumption(desired_consumption)
    elif option == '6':
        insert_car()

        #  add each attribute to the dictionary
        car_values = Dimensions
        car_values.update(Engine_Information)
        car_values.update(Fuel_Information)
        car_values.update(Identification)

        #  append the dictionary to the list
        #car1.append(car_values)
        #print('Successfully inserted !!!')

        #  load the file, append the data

        if path.isfile('Cars_test.json') is False:
            raise Exception('File not found')
        with open("Cars_test.json", "r+") as f:
            car1 = json.load(f)
            car1.append(car_values)
        with open("Cars_test.json", 'w') as fw:
            json.dump(car1, fw, indent=4, separators=(',', ': '))
        print('Successfully appended to Cars_test_Json')

    elif option == '7':
        update_car()
    elif option == '0':
        sys.exit()

    option1 = input('Do you want to continue add/edit/view details ? (Yes / no)')
    if option1.lower() == 'yes':
        get_option()
    else:
        sys.exit()


if __name__ == '__main__':
    Dimensions = {}
    Dimensions_Values = {}
    Engine_Information = {}
    Engine_Values = {}
    Engine_Statistics = {}
    Engine_Statistics_Values = {}
    Fuel_Information = {}
    Fuel_Information_Values = {}
    Identification_Values = {}
    Identification = {}
    car1 = []
    get_option()
