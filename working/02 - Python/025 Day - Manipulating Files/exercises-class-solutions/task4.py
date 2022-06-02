if __name__ == '__main__':

    # Solution 1
    with open('src/data/task4.txt') as file:
        file = file.read()
        print(file[1622:1635])

    # Shorter Solution 1
    with open('src/data/task4.txt') as file:
        print(file.read()[1622:1635])

