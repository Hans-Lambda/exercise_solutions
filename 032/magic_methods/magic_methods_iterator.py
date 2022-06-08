class EvenNumbers:

    def __init__(self, limit):
        self.counter = -2
        self.limit = limit

# __iter__() only works if accompanied by __next__()
    def __iter__(self):
        return self

    def __next__(self):
        if self.counter >= self.limit:
            raise StopIteration()       # https://www.w3schools.com/python/gloss_python_iterator_stop.asp

        self.counter += 2
        return f"The number is {self.counter}"


if __name__ == '__main__':

# iter() is necessary
    sequence = iter(EvenNumbers(limit=50))

#    print(next(sequence))

    for num in sequence:
        print(num)
