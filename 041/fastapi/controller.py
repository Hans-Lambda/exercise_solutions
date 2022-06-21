import db
import re


bikes = db.bikes


def list_bikes():
    return bikes


def list_bikes_by_manufacturer(manufacturer):

    return [bike for bike in bikes if re.findall(manufacturer.lower(), bike.manufacturer.lower())]


def list_bikes_by_name(name):

    return [bike for bike in bikes if re.findall(name.lower(), bike.name.lower())]


def add_bike(bike):

    bikes.append(bike)


def remove_bike(id_: str):

    [bikes.remove(bike) for bike in bikes if id_ == bike.id_]


def save_to_file():

    with open('/bikes.items', 'w'):
        pass

def load_file():

    with open('/bikes.items', 'r') as fp:
        fp.read()
