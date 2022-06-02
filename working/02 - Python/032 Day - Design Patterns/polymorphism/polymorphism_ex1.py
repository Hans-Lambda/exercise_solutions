from abc import ABC, abstractmethod

# https://www.geeksforgeeks.org/polymorphism-in-python/

class Animal(ABC):

#   @abstractmethod
    def print(self):
        print("I am an animal...")


class Dog(Animal):

    def print(self):
        print("I am a dog...")


class Cat(Animal):

    def print(self):
        print("I am a cat...")


class Bird(Animal):

# error, because Bird class wants to initiate print function, but has none
# to fix, remove abstractmethod in Animal

    def output(self):
        print("I am a bird...")

    # def print(self):
    #     print("This would work...")


if __name__ == '__main__':
    d = Dog()
    c = Cat()
    b = Bird()
    a = Animal()

    list_of_animals = [d, c, b, a]

    for animal in list_of_animals:
        animal.print()
