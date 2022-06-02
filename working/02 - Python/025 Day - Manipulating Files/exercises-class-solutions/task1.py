if __name__ == '__main__':
    # Almost a solution - 3 lines (instructions)
    file = open('src/data/task1.txt')
    print(file.read())
    file.close()

    # Solution - 2 lines (instructions)
    with open('src/data/task1.txt') as file:
        print(file.read())
