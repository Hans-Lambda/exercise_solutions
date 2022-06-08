import click

# https://github.com/mathiasbrito-dci/python-course-2022/blob/main/02%20-%20Python/024%20Day%20-%20Strings%20in%20Depth/EXERCISE-3.md

# Task 1

# The Secret of Love

def love():

    #You can use the singleton generator / list trick to avoid calling a function twice, but still reuse its result:

    secret = (next(x if len(x) >= 8 else input("Secret needs 8 characters as minimum: ") for x in [input("Please provide a secret: ")]))

    # secret = input("Please provide a secret: ") if len(list(locals().values())[0]) > 8 else input("Secret needs 8 characters as minimum: ")
    name = input("Please provide a your name: ")
    year = input("Please provide your year of birth: ")

    print(secret)
    print((secret + name)[::-1] + year)



if __name__ == '__main__':
    love()