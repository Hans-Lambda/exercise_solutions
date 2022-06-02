from dog import Dog
from animal import Animal


class GermanShepard(Dog):

    def walk(self):
        super().walk()
        Animal.some_method()
        print("German Shepard`s show their beautiful fur while running.")
