import json

# Task 2
#
# World Data - I Know everything
# Access the Website (Data World)[https://data.world/] (you need to register). There you will find hundreds of datasets,
# as json files, choose one that you find interesting. Create a program to load it as a dictionary. Discuss with your
# colleague what kind of relevant or interesting data can you extract from the dataset, and try to process it,
# e.g. calculate the average, mins and maxs, most frequent values, etc. Create a menu, so that the user can
# choose which kind of information it wants to extract.


def load_json():
    with open("/home/user/PycharmProjects/python-course-2022_part1/02 - Python/026 Day - Manipulating Files/"
              "exercise/owid-energy-data.json") as file:
        return json.load(file)

def fuck_around():
    data = load_json()

if __name__ == '__main__':
    fuck_around()
