def f(*args):
    total = 0
    for arg in args:
        total += arg
    return total


def g(x, y, z):
    return x + y + z


if __name__ == '__main__':
    print(f(1, 3, 4, 5, 6, 7))
    print(g(1, 3, 4))
