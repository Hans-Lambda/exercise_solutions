cars = [
    {"name": "ferrari", "cost": 8, "color": "red", "engine": "v12"},
    {"name": "porsche", "cost": 6, "color": "gray", "engine": "v10"},
    {"name": "lamborghini", "cost": 8, "color": "black", "engine": "v8"}
]


# Create a function that receives the data A, B, C, calculate the sum of three integer values A, B and C,
# and return the result.
def x(a, b, c):
    result = a + b + c
    return result


if __name__ == '__main__':
    print(x(1, 2, 3))

    t = 3
    g = 4
    d = 5

    print(x(t, g, d))

    r = x(9, 10, 1)
    r = r + 10
    print(r)

