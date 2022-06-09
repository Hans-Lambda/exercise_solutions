
def greeting(greeting_fun, name):
    greeting_fun(f"Hi {name}")

def greeting1(basic_greeting):
    print(f"{basic_greeting} - This is greeting 1 !")

def greeting2(basic_greeting):
    print(f"{basic_greeting} - This is greeting 2 !")


if __name__ == '__main__':
    greeting(greeting1, "Franz")
    greeting(greeting2, "Hans Lambda")
    greeting2("Hello")
