from pydantic import BaseModel
import pickle


class Bike(BaseModel):

    id_: str
    name: str
    manufacturer: str
    year: str
    #partner: Partner


def load_data():
    with open('data.pickle', 'rb') as file:
        bikes_loaded = pickle.load(file)

        for bike in bikes_loaded:
            print(f"{bike.name} made by {bike.manufacturer}")


def store_data():

    with open('data.pickle', 'wb') as file:
        pickle.dump(bikes, file)


bikes = [
    Bike(id_="agaag", name="Adventure Pro", manufacturer="TREK", year="2002-06-20T10:05:05.559000+00:00"),
    Bike(id_="36hds", name="Bullshit Pro", manufacturer="Bulls", year="2017"),
    Bike(id_="alfi7", name="Standard DDR Gedöns", manufacturer="Diamant", year="1986"),
    Bike(id_="afna5", name="E-Bike", manufacturer="KTM", year="2002"),
    Bike(id_="alh47", name="Fuck Jeff Bezos", manufacturer="Amazon", year="666"),
    Bike(id_="afaf5", name="Shitty E-Bike", manufacturer="KTM", year="6969")
]

clients = []

partners = []

bills = []


if __name__ == '__main__':

    store_data()
    load_data()
