
# https://github.com/mathiasbrito-dci/python-course-2022/blob/main/02%20-%20Python/024%20Day%20-%20Strings%20in%20Depth/EXERCISE-2.md

# String Basics 2

# Task 1:

def length():
    text = "Berlin is a world city of culture, politics, media and science."
    print(len(text))

# Task 2:

def first_last():
    text = "Berlin is a world city of culture, politics, media and science."
    print(text[0], text[-1])

# Task 3

def first_three():
    text = "Berlin is a world city of culture, politics, media and science."
    print(f"First three characters: {text[:3].upper()}")

# Task 4

def count_letters():
    text = "Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital"
    print(f'B appears: {text.count("B")} times')

# Task 5

def last_ten():
    text = "Berlin straddles the banks of the Spree, which flows into the Havel (a tributary of the Elbe) in the western borough of Spandau."
    print(f"Last ten characters: {text[-10:]}")

# Task 6

def remove_hyphen():
    text = "---Python programming---"
    print(text.replace("-", ""))

# Task 7

def string_concatenate():
    firstname = "Franz"
    lastname = "Bandelin"
    [print(f"{k.capitalize()}: {v}") for k, v in locals().items()]

if __name__ == '__main__':
    length()
    first_last()
    first_three()
    count_letters()
    last_ten()
    remove_hyphen()
    string_concatenate()
