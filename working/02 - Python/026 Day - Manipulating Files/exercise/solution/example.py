import json


if __name__ == '__main__':

    # Download the file from https://nyc3.digitaloceanspaces.com/owid-public/data/energy/owid-energy-data.json
    with open('owid-energy-data.json') as file:
        data = json.load(file)

    country = input("Type a country's name: ")
    total = 0

    for record in data[country]['data']:
        if 'coal_production' in record.keys():
            total = total + record['coal_production']

    print(total)

    for key, value in data.items():
        print(key)
