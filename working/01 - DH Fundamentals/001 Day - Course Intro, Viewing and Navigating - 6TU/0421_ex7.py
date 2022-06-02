def month(d):
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    print(f"{months[d - 1]}")


if __name__ == '__main__':
    m = int(input("Please type the number of the month: "))
    month(m)

