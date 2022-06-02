if __name__ == '__main__':

    file = open('csv_values.txt')

    for line in file.readlines():
        print(line, end='')
        print(line.split(';'))

    file.close()
