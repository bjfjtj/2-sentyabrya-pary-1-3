# Задача 7 – Полиморфизм: переопределение draw()

## Условие
Добавьте в базовый класс `Figure` метод `draw()`, который просто выводит «Рисуется фигура». Переопределите этот метод в дочерних классах (`Line`, `Rect`, `Ellipse`), чтобы каждый выводил своё специфичное сообщение (например, «Рисуется линия...»).

В главной программе создайте один общий список, в который положите объекты всех трёх типов. Напишите один цикл `for`, который проходит по списку и вызывает `draw()` для каждого элемента.

## Решение
В базовом классе определён метод `draw()`. В каждом дочернем классе он переопределён. Благодаря полиморфизму при вызове `draw()` в цикле выполняется нужная версия метода для каждого объекта, независимо от его типа.

## Код
```python
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