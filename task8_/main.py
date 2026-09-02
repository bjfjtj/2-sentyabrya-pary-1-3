# Базовый класс Figure (из задачи 5/6/7)
class Figure:
    def __init__(self, coords=(0, 0), width=1, color="black"):
        self.coords = coords
        self.width = width
        self.color = color

    def draw(self):
        print("Рисуется фигура")


# Дочерние классы из задачи 6 и 7
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


# Новый класс Triangle (задача 8)
class Triangle(Figure):
    def __init__(self, coords, width, color, side_length):
        super().__init__(coords, width, color)
        self.side_length = side_length

    def draw(self):
        print("Рисуется треугольник...")


# Главная программа (цикл из задачи 7, не изменён)
figures = [
    Line((0, 0), 1, "blue", 10),
    Rect((2, 3), 4, "green", 5),
    Ellipse((5, 5), 6, "yellow", 3),
    Triangle((1, 1), 2, "red", 7)   # новый объект
]

# Цикл остался без изменений
for fig in figures:
    fig.draw()