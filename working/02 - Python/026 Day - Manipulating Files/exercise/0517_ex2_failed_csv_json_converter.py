import csv
import json
import pandas as pd


def load_json():
    with open("/home/user/PycharmProjects/python-course-2022_part1/02 - Python/026 Day - Manipulating Files/exercise/"
              "total-affected-natural-disasters-csv-1.json") as file:
        return json.load(file)

def fuck_around():
    data = load_json()

    [print(f'In {entry["Country Name"]} about {entry["2014"]} where affected by natural disasters in the year 2014') for entry in data if entry["2014"]]


if __name__ == '__main__':

    # csvFilePath = "/home/user/PycharmProjects/python-course-2022_part1/02 - Python/026 Day - Manipulating Files/exercise/Germany_Human_Development_Indicators/hdro-faae6f89-c734-4792-be4c-133a1c819588/human-development-indicators-for-germany-1.csv"
    # jsonFilePath = "/home/user/PycharmProjects/python-course-2022_part1/02 - Python/026 Day - Manipulating Files/exercise/Germany_Human_Development_Indicators/hdro-faae6f89-c734-4792-be4c-133a1c819588/human-development-indicators-for-germany-1.json"
    #
    # data = {}
    #
    # with open(csvFilePath, encoding='utf-8') as csvFile:
    #     csvReader = csv.DictReader(csvFile)
    #     for rows in csvReader:
    #         key = rows['#country+code']
    #         data[key] = rows
    #
    # print(data)
    #
    # with open(jsonFilePath, mode='w', encoding='utf-8') as jsonFile:
    #     jsonFile.write(json.dumps(data, indent=4))


    df = pd.read_csv (r'/home/user/PycharmProjects/python-course-2022_part1/02 - Python/026 Day - Manipulating Files'
                      r'/exercise/Germany_Human_Development_Indicators/hdro-faae6f89-c734-4792-be4c-133a1c819588'
                      r'/human-development-indicators-for-germany-1.csv')
    df.to_json (r'/home/user/PycharmProjects/python-course-2022_part1/02 - Python/026 Day - Manipulating Files/exercise'
                r'/Germany_Human_Development_Indicators/hdro-faae6f89-c734-4792-be4c-133a1c819588'
                r'/human-development-indicators-for-germany-1.json')


