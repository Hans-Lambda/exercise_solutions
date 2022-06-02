# data structure


# -- how is our data storage designed?

# data types
# - numbers
# - strings
# - etc. ()

student1 = "ikoro"
student2 = "elina"
## too many students
student10000 = "Alex"
# list of things
students = [ "ikoro", "elina", "alex", 'Hilz']
# we want to send a message to each student

# local variable, temporary
def func(students):
    for student in students:
        # return student
        print(f"Hello {student}")
    # return ""

# print(func(students))


# when do I use return or not?
# def add(a, b):
#     return a + b

# adder = add(4, 5)
# print(adder)