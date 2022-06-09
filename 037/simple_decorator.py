
def simple_decorator(func):

    def wrapper():
        print("Something before calling greeting")
        greeting_string = func()
        greeting_string = f'{greeting_string}, Welcome to DCI!!'
        print("Something after calling greeting")
        return greeting_string

    return wrapper


@simple_decorator
def greeting():
    #print("Hi")
    return "Hi"


@simple_decorator
def greeting2():
    return "Dear Sir Franz"


if __name__ == '__main__':
    value = greeting()
    print(value)
    print(greeting2())
