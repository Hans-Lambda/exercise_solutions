if __name__ == '__main__':

    with open('data.txt') as file:
        for line in file:
            print(line)

    with open('data.txt') as file:
        lines = list(file)
        print(lines)
