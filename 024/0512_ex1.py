
# https://github.com/mathiasbrito-dci/python-course-2022/blob/main/02%20-%20Python/024%20Day%20-%20Strings%20in%20Depth/EXERCISE-1.md

# String Basics 1

# Task 1

def city():
    city = "London"
    print(city)


# Task 2

def cap_city():
    city = "Berlin"
    population = 3645000
    print(f"{city}: {population}")


# Task 3

def bool_city():
    city = "Berlin"
    population = 9000000
    # dict of k: v // variable names: variables
    # use globals() if function on top level like main()
    #variable_names = [name for name in locals() if locals()[name] is city or population]
    # print(variable_names)
    # print(locals().items())
    [print(f"{k.capitalize()}: {v.capitalize() if (type(v) == str) else v} {f'({type(v) == str})' if type(v) == str else ''}") for k, v in locals().items()]

# Task 4

def check_city():
    text = "Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital."
    print(f'capital: {text.find("capital")}')

# Task 5

def split_city():
    text = "Berlin straddles the banks of the Spree, which flows into the Havel (a tributary of the Elbe) in the western borough of Spandau."
    print(text.split())

# Task 6

def replace_city():
    text = "Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital."
    print(text.replace("capital", "capital of Germany"))


if __name__ == '__main__':
    #city()
    #cap_city()
    #bool_city()
    #check_city()
    #split_city()
    replace_city()

