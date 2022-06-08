def check_distance_limit(distance, limit):
    return distance > limit


if __name__ == '__main__':
    distance = int(input("What is the distance? "))
    fuel = int(input("How much fuel did you use? "))
    has_fuel = fuel > 0
    # renting cars, they give you limits - 500km
    limit = 500
    if check_distance_limit(distance, limit):
        print("You have to pay more money! ", (distance - limit) * 0.5, "Euro")
    if has_fuel:
        print("Distance / l", distance / fuel, 'km/l')
    else:
        print("Fill up your tank!")
