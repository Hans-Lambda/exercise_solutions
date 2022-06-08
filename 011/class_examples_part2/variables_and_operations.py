def f(a, b):
    return (a + b + 3)/2


def g(x, y):
    print("Calculating function G")
    return (x + y) * x


def check_age(age):
    return age >= 18


if __name__ == '__main__':
    a = 2
    b = 3
    c = (a + b + 3)/2
    print(c)
    c = f(a, b)
    print(c)
    d = g(a, b)
    print(d)
    check = check_age(21)
    print(check)
