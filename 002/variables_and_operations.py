
# Introduction

# "def" creates a function "def NAME(parameter, param, ..):"

def f(a, b):
    return (a + b + 3) / 2


def g(x, y):
    print("Calculating function G")
    print("Fuck Igor")
    return(x + y) * x


def check_age(age):
    return age >= 18


# main function is starting point for interpreter

if __name__ == '__main__':
    a = 2
    b = 3
    c = (a + b + 3) / 2
    print(c)
    c = f(a, b)
    print(c)
    d = g(a, b)
    print(d)
    # check variable has check_age function as value
    check = check_age(36)
    print(check)

# test driven development
