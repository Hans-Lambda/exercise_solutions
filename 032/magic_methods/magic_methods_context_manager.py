# https://blog.finxter.com/python-__enter__-magic-method/
# https://docs.python.org/3/library/stdtypes.html#typecontextmanager

# with open("filename") as f:
#     f.read()
#     f.close()

# x = 1
# y = 7
# z = x + y

class HTTPConnection:

    def __init__(self, address):
        self.address = address

    def __enter__(self):
        print(f"connected to {self.address}")
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        print(f"Closing the connection...")
        # ToD: logic for closing connection
        print(f"Connection Closed...")

    def send(self):
        print("Simulate sending data...")


if __name__ == '__main__':

    with HTTPConnection("192.168.0.1") as connection:
        print(connection)
        connection.send()
        connection.send()
        connection.send()

    print("Out of Context Manager")
