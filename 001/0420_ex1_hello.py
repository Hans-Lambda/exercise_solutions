# f strings to insert stuff like NAME, f"...{NAME}.."


def hello(g, n):
    print(f"{g} {n}, you fucking genius!")


if __name__ == '__main__':
    name = input("Type your name please: ")
    hello("Hello", name)




