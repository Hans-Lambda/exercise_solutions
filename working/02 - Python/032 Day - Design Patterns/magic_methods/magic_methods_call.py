class Car:

    def __init__(self):

        self.current_speed = 0
        self.list = ["apple", "mongo", "banana"]

    def print(self):
        print(f"I am a car at {self.current_speed}")
        print(self.list)

    def __call__(self, *args, **kwargs):
        print("I can be called now")


if __name__ == '__main__':

    car1 = Car()

# makes it possible to call objects
    car1()
    car1.print()
