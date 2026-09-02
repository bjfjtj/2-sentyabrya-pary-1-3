class Figure:
    def __init__(self, coords=(0, 0), width=1, color="black"):
        self.coords = coords
        self.width = width
        self.color = color

    def display(self):
        print(f"Фигура: {self.__class__.__name__}, координаты {self.coords}, ширина {self.width}, цвет {self.color}")

class Line(Figure):
    def __init__(self, coords, width, color, length):
        super().__init__(coords, width, color)
        self.length = length

class Rect(Figure):
    def __init__(self, coords, width, color, height):
        super().__init__(coords, width, color)
        self.height = height

class Ellipse(Figure):
    def __init__(self, coords, width, color, radius):
        super().__init__(coords, width, color)
        self.radius = radius

# Создание объектов
line = Line((0, 0), 1, "blue", 10)
rect = Rect((2, 3), 4, "green", 5)
ellipse = Ellipse((5, 5), 6, "yellow", 3)

# Вывод
line.display()
rect.display()
ellipse.display()