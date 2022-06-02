from german_shepard import GermanShepard
from dog import Dog


class Test(GermanShepard):

    def walk(self):
        super().walk()
        print("Let's see if really every version of walk is called")

    def breathe(self):
        super().breathe()
        print("Test likes to breathe.")
        Dog.breathe(self)

