
def repeat(num=1):
    def decorator(func):

        def wrapper(*args, **kwargs):

            for i in range(num):
                func()

        return wrapper

    return decorator


def greeting_selector(greeting_type="formal"):
    def formal_decorator(func):
        def wrapper(*args):
            print(f"Hi {args[0]} {func(args[0])}, how are you?")

        return wrapper

    def informal_decorator(func):
        def wrapper(*args):
            print(f"Hello dear Sir or Madam {args[0]} {func(args[0])}, how are you?")

        return wrapper

    if greeting_type == "formal":
        return formal_decorator
    else:
        return informal_decorator


@repeat(3)
def greeting():
    print("Hi")


@greeting_selector(greeting_type="informal")
def greeting2(name):
    return f"Thanks I am {name}"

if __name__ == '__main__':

    greeting()
    greeting2("Franz")

