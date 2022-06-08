import json
import pyfiglet
import sys

# The "Super Car Store" is an auto megastore. You can find there any car you can imagine, its owner cataloged all the
# cars in a file and a company developer created a list of dictionaries out of it. You can find the data in the file
# car.py, and a small subset of the data in cars_small.
#
# The owner intended to have a computer program to help in the management of the store, allowing him to find some model
# details easily for example, or to filter the cars' list based on specific criteria.
#
# You have to create a program with the following functions:
#
# def get_car_by_name(name)
# def get_car_by_number_of_gears(number_of_gears)
# def get_car_by_manufacturer(manufacturer)
# def get_car_by_average_comsumption(desired_consumption)
# def get_car_by_year(year)
# Every function will return a list of the cars that match the criteria. For checking by name use the function/method
# of string variables called find it will return the position in the string where the first occurrence of the word
# appears or -1 if nothing is found. E.g.


def get_car_by_name(cars_list):
    name = input("Please type car ID: >>> ")
    print("Search Results:")
    [print(x["Identification"]["ID"]) for x in cars_list if x["Identification"]["ID"].upper().find(name.upper()) != -1]
    result = [x for x in cars_list if x["Identification"]["ID"].upper().find(name.upper()) != -1]

    if len(result) > 1:
        narrow(result)
    else:
        return result


def get_car_by_number_of_gears():
    number_of_gears = int(input("Please type number of desired gears: >>> "))
    print("Search Results:")
    [print(x["Identification"]["ID"]) for x in cars_list if x["Engine Information"]["Number of Forward Gears"] == number_of_gears]


def get_car_by_manufacturer():
    manufacturer = input("Please type the desired manufacturer: >>> ")
    print("Search Results:")
    [print(x["ID"]) for x in [x["Identification"] for x in cars_list] if x["Make"].upper().find(manufacturer.upper()) != -1]


def get_car_by_average_comsumption():
    desired_consumption = float(input("Please type the minimal average gpm: >>> "))
    print("Search Results:")
    [print(car["Identification"]["ID"]) for car in cars_list for item in car["Engine Information"] if (car["Fuel Information"]["City mpg"] + car["Fuel Information"]["Highway mpg"]) / 2 > desired_consumption]


def get_car_by_year():
    year = int(input("Please type year: >>> "))
    print("Search Results:")
    [print(x["ID"]) for x in [x["Identification"] for x in cars_list] if x["Year"] == year]


# Inserting new cars into the list
# Write a function that receives a dictionary with information about a new car and inserts it in the car's list.
# Read from the user the data of the new car.


def insert_car():
    car = {
        "Dimensions": {
            "Height": 0,
            "Length": 0,
            "Width": 0
        },
        "Engine Information": {
            "Driveline": "empty",
            "Engine Type": "empty",
            "Hybrid": True,
            "Number of Forward Gears": 0,
            "Transmission": "empty",
            "Engine Statistics": {
                "Horsepower": 0,
                "Torque": 0
            }
        },
        "Fuel Information": {
            "City mpg": 0,
            "Fuel Type": "empty",
            "Highway mpg": 0
        },
        "Identification": {
            "Classification": "empty",
            "ID": "empty",
            "Make": "empty",
            "Model Year": "empty",
            "Year": 0
        }
    }
    print("You will now add a new car, step by step!")
    for info in car:
        for prop in car[info]:
            if prop == "Engine Statistics":
                for stat in car[info][prop]:
                    car[info][prop][stat] = input(f"Please update the {info} by providing the following information: {prop}, {stat}: >>> ")
            else:
                car[info][prop] = input(f"Please update the {info} by providing the following information: {prop}: >>> ")
        break
    cars_list.append(car)
    print("You successfully added the following car:")
    print(cars_list[-1]["Identification"]["ID"])


def updating_car():
    [car] = get_car_by_name()
    change = input("Please provide the parameter you would like to update")
    for info in car:
        for prop in car[info]:
            if prop == "Engine Statistics":
                for stat in car[info][prop]:
                    if stat.upper().find(change.upper()) != -1:
                        car[info][prop][stat] = input(f"Please update the {info} by providing the following information: {prop}, {stat}: >>> ")
            if prop.upper().find(change.upper()) != -1:
                car[info][prop] = input(f"Please update the {info} by providing the following information: {prop}: >>> ")
    if [dict] in cars_list:
        cars_list[dict] = car
    print(f'You successfully updated {car["Identification"]["ID"]}')
    [print(x) for x in cars_list if x == car]



# this narrows down the results of get_car_by_name to 1 result
def narrow(result):

    if len(result) == 2 and result[0]["Identification"]["ID"] == result[1]["Identification"]["ID"]:
        print(f"this is shit {result[0]}")
        return result[0]
    else:
        while not (len(result) == 2):
            print("Please specify")
            get_car_by_name(result)
            return result


# my fancy search, try anything
def search():
    searchterms = (input("Please enter your searchterms:")).upper().split()
    print(f"You looked for the following:\n{searchterms}")
    cars_db = json.load(open('../022 Day/cars.json', 'r'))
    for term in searchterms:
        cars_db = [car for car in cars_db for k, v in car.items() if (str(k).upper().find(str(term)) != -1) or (str(v).upper().find(str(term)) != -1)]
        print(len(cars_db))
    [print(car["Identification"]["ID"]) for car in cars_db]
    exit = input("Type Y to search again or any key to exit.")
    if exit in ["Y", "y"]:
        search()
    else:
        sys.exit()


def menu():
    heading = pyfiglet.figlet_format("Main Menu", font="slant")

    print(heading)
    print("""        
        1. Search for car by name
        2. Search for car by manufacturer
        3. Search for car by number of gears
        4. Search for car by average consumption
        5. Search for car by year 
        6. Insert new car
        7. Update existing car
        8. Epic Search
        0. Exit
        """)

    choice = int(input("Please choose by typing the corresponding number: "))
    while choice != 0:
        if choice == 1:
            get_car_by_name(cars_list)
            menu()
        elif choice == 2:
            get_car_by_manufacturer()
            menu()
        elif choice == 3:
            get_car_by_number_of_gears()
            menu()
        elif choice == 4:
            get_car_by_average_comsumption()
            menu()
        elif choice == 5:
            get_car_by_year()
            menu()
        elif choice == 6:
            insert_car()
            menu()
        elif choice == 7:
            updating_car()
            menu()
        elif choice == 8:
            search()
            menu()
        else:
            print("Please choose a correct number")
            menu()


def lama(name):
    list_by_name = []
    [print(car_name) for car_name in [list_by_name.append(car["Identification"]["ID"]) or car for car in cars_list if car["Identification"]["ID"].upper().find(name.upper()) != -1]]


if __name__ == '__main__':
    cars_list = json.load(open('../022 Day/cars.json', 'r'))
    menu()
    #search()


