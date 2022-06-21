import pickle


data = []


def store_data():
    with open('new.pickle', 'wb') as file:
        pickle.dump(data, file)


def load_data():

    try:
        with open('new.pickle', 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        store_data()
        return []
