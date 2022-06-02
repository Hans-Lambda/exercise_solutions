

def sum3(numbers=[1, 2, 3]):
    print(sum(numbers))
    return sum(numbers)


if __name__ == '__main__':
    a = int(input("Type first number: "))
    b = int(input("Type second number: "))
    c = int(input("Type third number: "))
    numbers = [a, b, c]
    sum3(numbers)
