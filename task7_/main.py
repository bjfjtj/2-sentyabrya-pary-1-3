class Figure:
    def __init__(self, coords=(0, 0), width=1, color="black"):
        self.coords = coords
        self.width = width
        self.color = color

    def draw(self):
        print("Рисуется фигура")

class Line(Figure):
    def __init__(self, coords, width, color, length):
        super().__init__(coords, width, color)
        self.length = length

    def draw(self):
        print("Рисуется линия...")

class Rect(Figure):
    def __init__(self, coords, width, color, height):
        super().__init__(coords, width, color)
        self.height = height

    def draw(self):
        print("Рисуется прямоугольник...")

class Ellipse(Figure):
    def __init__(self, coords, width, color, radius):
        super().__init__(coords, width, color)
        self.radius = radius

    def draw(self):
        print("Рисуется эллипс...")

# Создание списка фигур
figures = [
    Line((0, 0), 1, "blue", 10),
    Rect((2, 3), 4, "green", 5),
    Ellipse((5, 5), 6, "yellow", 3)
]

# Единый цикл для всех фигур
for fig in figures:
    fig.draw()