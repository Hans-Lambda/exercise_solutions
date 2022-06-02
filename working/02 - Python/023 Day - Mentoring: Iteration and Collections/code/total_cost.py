cars = [
    {"name": "ferrari", "cost": 80000, "color": "red", "engine": "v12"},
    {"name": "porsche", "cost": 60000, "color": "gray", "engine": "v10"},
    {"name": "lamborghini", "cost": 80503, "color": "black", "engine": "v8"}
]

# Create a function that receives a list with cars and return the sum of the cars' price.


def get_total_cost(cars_list):
    total = 0
    for car in cars_list:
        total = total + car["cost"]

    return total


if __name__ == '__main__':
    cost = get_total_cost(cars)
    print(cost)
