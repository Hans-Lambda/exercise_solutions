import json

if __name__ == '__main__':

    # Loading the data
    with open('simple_object.json') as file:
        data = json.load(file)
        print(data["name"])

    # Changing an existent key value
    data["name"] = input("Type a name: ")
    with open('simple_object.json', mode='w') as file:
        json.dump(data, file, indent=2)

    # Adding a key-value pair
    key = input("type a new key: ")
    value = input("type the value: ")
    data[key] = value
    with open('simple_object.json', mode='w') as file:
        json.dump(data, file, indent=2)
