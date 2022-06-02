if __name__ == '__main__':

    # Solution 1 (using subtraction)
    with open('src/data/task2.txt') as file:
        lines = list(file)
        print(len(lines) - 2)

    # Solution 2 (using list slicing)
    with open('src/data/task2.txt') as file:
        lines = list(file)
        print(len(lines[2:]))

    # Solution 3 (using readlines)
    with open('src/data/task2.txt') as file:
        lines = file.readlines()
        print(len(lines) - 2)  # or `print(len(lines[2:]))`