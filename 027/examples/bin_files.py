if __name__ == '__main__':

    with open('file1.bin', 'wb') as file:
        file.write(b'2022')

    with open('file2.bin', 'wb') as file:
        file.write(int(255).to_bytes(1, 'big'))

    with open('file3.bin', 'wb') as file:
        file.write(int(2022).to_bytes(2, 'big'))

    with open('file3.bin', 'rb') as file:
        b = file.read()
        print(int.from_bytes(b, "big"))

    with open('file1.bin', 'rb') as file:
        b = file.read()
        print(str(b, 'utf-8'))
