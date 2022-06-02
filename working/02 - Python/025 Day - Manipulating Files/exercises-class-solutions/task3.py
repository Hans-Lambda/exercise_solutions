if __name__ == '__main__':

    # First Solution (with slicing)
    with open('src/data/task3.txt') as file:
        lines = file.readlines()  # or lines = list(file)

        for line in lines:
            print(line, end='')

        print('\n------------\n')

        odds = lines[::2]
        even = lines[1::2]

        for line in odds:
            print(line, end='')

        for line in even:
            print(line, end='')

    print('\n----------\n------------\n---------')

    # Second Solution with %
    with open('src/data/task3.txt') as file:
        lines = file.readlines()  # or lines = list(file)

        for line in lines:
            print(line, end='')

        print('\n------------\n')

        for index in range(len(lines)):
            if index % 2 == 0:
                print(lines[index], end='')

        for index in range(len(lines)):
            if index % 2 == 1:
                print(lines[index], end='')
