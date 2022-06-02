class Rectangle:

    def __init__(self):
        self.width = 1
        self.height = 1

    def increase_height(self):
        self.height += 1


if __name__ == '__main__':
    print("Our program is running...")

    rect1 = Rectangle()
    rect2 = Rectangle()
    rect3 = Rectangle()

    print(rect1.height)
    print(rect2.height)
    print(rect3.height)

    rect1.increase_height()
    rect1.increase_height()

    print(rect1.height)
    print(rect2.height)
    print(rect3.height)

