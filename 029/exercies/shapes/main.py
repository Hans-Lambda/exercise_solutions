from canvas import Canvas
from shapes import Rectangle, Triangle
from shapes import Pentagon, Circle


if __name__ == '__main__':
    canvas = Canvas()

    rectangle1 = Rectangle(5, 4)
    triangle1 = Triangle(4, 5, 6)
    circle1 = Circle(8)
    pentagon1 = Pentagon(3)

    canvas.add_shape(rectangle1)
    canvas.add_shape(triangle1)
    canvas.add_shape(circle1)
    canvas.add_shape(pentagon1)

    canvas.print()
