if __name__ == '__main__':

    with open('data.txt') as file:
        content = file.read()
        print(len(content))
        print(content.find('line'))
