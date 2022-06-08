from sum_numbers import sum_lists

cars = [
    {"name": "ferrari", "cost": 8, "color": "red", "engine": "v12"},
    {"name": "porsche", "cost": 6, "color": "gray", "engine": "v10"},
    {"name": "lamborghini", "cost": 8, "color": "black", "engine": "v8"}
]

l1 = [1, 2, 3, 4, 5]
l2 = [9, 3, 4, 6, 4]

result = []
for value in cars:
    result.append(value["name"])

print(result)

for car_name in result:
    print(car_name)
