def dig_3(a):
    return "{:.3f}".format(a)


def consumption(a, b):
    print(f"{dig_3(a / b)} km/l")


if __name__ == '__main__':
    distance = float(input("Please type the distance: "))
    fuel = float(input("Please type the amount of used fuel: "))
    consumption(distance, fuel)
