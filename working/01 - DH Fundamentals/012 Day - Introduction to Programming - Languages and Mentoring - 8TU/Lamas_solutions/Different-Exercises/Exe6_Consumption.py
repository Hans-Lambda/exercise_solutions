def ave_cons(d, f):
    return "{:.3f}".format(d/f)


if __name__ == '__main__':
    # ignored the error could happen when the user enters values like 20 km or 50 liter
    distance = float(input("Enter the distance you traveled in km (only value  without unit): "))
    fuel = float(input("Enter the spent fuel total in Liter (only value without unit): "))
    print(f"{ave_cons(distance, fuel)} km/l")