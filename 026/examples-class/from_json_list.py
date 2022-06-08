import json

if __name__ == '__main__':

    # Loading the data...
    with open('list.json') as file:
        data = json.load(file)
        print(data)
        print(f'loaded data is from type: {type(data)}')
        print(f'data elements area from type {type(data[0])}')

    # Changing the value of a key in an existent record (dict/json object)
    print(data[2]["name"])
    data[2]["name"] = input("type a new name for record two: ")
    with open('list.json', mode='w') as file:
        json.dump(data, file, indent=2)

    # Adding a new record
    record = {}
    record["name"] = "New User"
    data.append(record)
    with open('list.json', mode='w') as file:
        json.dump(data, file, indent=2)
