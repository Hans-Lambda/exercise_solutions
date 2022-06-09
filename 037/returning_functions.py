
def formal_greeting(name):
    print(f"Dear Sir {name}")


def informal_greeting(name):
    print(f"Hello {name}")


def greeting_selector(option):
    if option == 1:
        return formal_greeting
    else:
        return informal_greeting


if __name__ == '__main__':

    print("1. Formal")
    print("2. Informal")
    option = int(input("What greeting should I use? "))

    greeting = greeting_selector(option)
    greeting("Franz")
