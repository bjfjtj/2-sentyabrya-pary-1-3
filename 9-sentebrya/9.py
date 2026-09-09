class Figure:
    def __init__(self, coords, width, color):
        self.coords = coords
        self.width = width
        self.color = color

    def draw(self):
        print("Рисуется фигура")

class Line(Figure):
    def draw(self):
        print("Рисуется линия")

class Rect(Figure):
    def draw(self):
        print("Рисуется прямоугольник")

class Ellipse(Figure):
    def draw(self):
        print("Рисуется эллипс")

# Дополнительный класс Triangle для добавления позже
class Triangle(Figure):
    def draw(self):
        print("Рисуется треугольник")

# Создаём список объектов
figures = [
    Line((0,0,10,10), 2, "red"),
    Rect((0,0,20,20), 1, "blue"),
    Ellipse((5,5,15,15), 3, "green")
]

# Цикл для отрисовки
for fig in figures:
    fig.draw()

# Добавляем треугольник и снова проходим по циклу (можно просто расширить список)
figures.append(Triangle((1,1,2,2), 1, "yellow"))
for fig in figures:
    fig.draw()