
def named_greeting(func):

    def wrapper(*args, **kwargs):
        name = args[0]
        name = name.upper()
        greeting_str = func(name, **kwargs)

        # setting default in wrapper
        # city = kwargs.setdefault('city', 'Berlin')
        # city = city.upper()
        # greeting_str = func(name, city=city)

        # this would work if the city argument was provided correctly
        # city = kwargs['city']
        # city = city.upper()
        # greeting_str = func(name, city=city)

        # we search for the city argument, because it is passed to the function but not mentioned before (main)
        # if "city" in kwargs:
        #     #city = kwargs['city']
        #     city = kwargs.get('city')
        #     city = city.upper()
        #     greeting_str = func(name, city=city)
        # else:
        #     greeting_str = func(name)

        return greeting_str

    return wrapper


@named_greeting     # @named_greeting(arguments possible, city="Berlin")
def greeting(name, city="Berlin"):      # default argument doesn't work here, because in main we provide only 1 argument
    return f"Dear Sir {name}, so you are from {city}?"


if __name__ == '__main__':
    print(greeting("Franz"))
    print(greeting("Franz", city="Greifswald"))
