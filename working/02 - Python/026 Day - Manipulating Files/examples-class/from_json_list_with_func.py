import json


def save_to_file(data):
    with open('list.json', mode='w') as file:
        json.dump(data, file, indent=2)


def load_my_file():
    with open('list.json') as file:
        return json.load(file)


if __name__ == '__main__':

    # Loading the data...
    data = load_my_file()
    print(data)
    print(f'loaded data is from type: {type(data)}')
    print(f'data elements area from type {type(data[0])}')

    # Changing the value of a key in an existent record (dict/json object)
    print(data[2]["name"])
    data[2]["name"] = input("type a new name for record two: ")
    save_to_file(data)

    # Adding a new record
    record = {}
    record["name"] = "New User"
    data.append(record)
    save_to_file(data)
