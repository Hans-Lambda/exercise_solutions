def greeting(first_name, last_name="Doe", age=25):

    print(f"Hi, Welcome to DCI {first_name} {last_name}!")
    print(f"I can see you are {age} years old!")
    print("Let's go!!!")

def greeting2(*args, **kwargs):

    for arg in args:
        print(arg, end=' ')
    print(kwargs["country"])

    if "country" in kwargs.keys():
        print(f"So, you are from {kwargs['country']}...")


if __name__ == '__main__':

    greeting("Franz", "du geile Sau", 36)
    greeting("Colonel", "Hans Lambda", 36)
    greeting("John", age=69)

    print("Franz", "Bandelin", 36, "Fuckstreet 69")

    greeting2("Franz", "Bandelin", 36, "Fuckstreet 69", country="Germany")
