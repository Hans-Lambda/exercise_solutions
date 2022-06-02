def f(**kwargs):
    for key, value in kwargs.items():
        print(f"The key is {key}, the value for this key is {value}")

    # Returns a default value if key doesn't exists
    # Do not add this key to the dictionary.
    print(kwargs.get("something", 1000))


if __name__ == '__main__':
    f(size=1, weight=3, age=4)
