class Canvas:

    def __init__(self):
        self.shapes = []

    def add_shape(self, shape):
        self.shapes.append(shape)

    def print(self):
        for shape in self.shapes:
            shape.print()
