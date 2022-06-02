cars = [
    {"name": "ferrari", "cost": 80000, "color": "red", "engine": "v12"},
    {"name": "porsche", "cost": 60000, "color": "gray", "engine": "v10"},
    {"name": "lamborghini", "cost": 80503, "color": "black", "engine": "v8"},
    {"name": "lamborghini", "cost": 80503, "color": "red", "engine": "v8"}
]

# Create a function that receives a list of  cars and a color and returns a list of cars of the specified color.


def get_cars_from_color(cars_list, color):
    result = []
    for car in cars_list:
        if car["color"] == color:
            result.append(car)

    return result


if __name__ == '__main__':
    res = get_cars_from_color(cars, "red")
    print(res)
