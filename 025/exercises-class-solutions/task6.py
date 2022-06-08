if __name__ == '__main__':

    # Solution 1 (using for loops to count)
    result = []
    with open('src/data/task6.txt') as file:
        for line in file:
            counter = 0
            for char in line:
                counter += 1
            result.append(counter)

        print(result)

    # Solution 2 (using for len - not allowed by the exercised)
    result = []
    with open('src/data/task6.txt') as file:
        for line in file:
            result.append(len(line))

        print(result)
