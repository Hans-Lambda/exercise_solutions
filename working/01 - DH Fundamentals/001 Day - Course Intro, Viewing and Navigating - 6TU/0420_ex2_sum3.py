def sum3(x, y, z):
    return x + y + z


# debugger - step over - execute next line
# debugger - step into - goes directly into function and shows values received
# debugger - click left of code to make breakpoint (below play symbol)


if __name__ == '__main__':
    result = sum3(1, 3, 4)
    print(result)
    a = 5
    b = 6
    c = 4
    result2 = sum3(a, b, c)
    print(result2)

    print(sum3(2, 3, a))
