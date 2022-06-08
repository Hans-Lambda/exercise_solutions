if __name__ == '__main__':

    # Solution 1
    with open('src/data/task5.txt') as file:
        line = file.readline()
        print(line)

        counter = 0
        for char in line:
            if char != '\n':
                counter += 1
        print(counter)

    # Solution 2
    with open('src/data/task5.txt') as file:
        line = file.readline().strip()

        counter = 0
        for char in line:
            counter += 1

        print(counter)
