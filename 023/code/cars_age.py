cars = [
    {"name": "ferrari", "cost": 80000, "color": "red", "engine": "v12", "age": 30},
    {"name": "porsche", "cost": 60000, "color": "gray", "engine": "v10", "age": 10},
    {"name": "lamborghini", "cost": 80503, "color": "black", "engine": "v8", "age": 1},
    {"name": "lamborghini", "cost": 80503, "color": "red", "engine": "v8", "age": 0}
]


def car_by_age(car_list, age):
    result = []
    for car in car_list:
        if car["age"] == age:
            result.append(car)

    return result


def get_average_cars_age(car_list):
    total = 0
    for car in car_list:
        total = total + car["age"]

    return total/len(car_list)


if __name__ == '__main__':
    age = int(input("type the age "))
    res = car_by_age(cars, age)

    print(res)

    average = get_average_cars_age(cars)
    print(f"The average age of the cars is: {average}")
