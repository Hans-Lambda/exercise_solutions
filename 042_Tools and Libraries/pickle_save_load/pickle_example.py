import pickle
import json


class Client:

    def __init__(self, name, age):

        self.name = name
        self.age = age


if __name__ == '__main__':

    client = [
        Client("Mathias", 39),
        Client("Franz", 36)
    ]

    # json.dump([{"name": "Mathias", "age": 39}])

    # 'wb' to write to binary file
    with open('clients.pickle', 'wb') as file:
        pickle.dump(client, file)

    with open('clients.pickle', 'rb') as file:
        clients_loaded = pickle.load(file)

        for client in clients_loaded:
            print(client.name)
