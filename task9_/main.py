class Figure:
    def __init__(self, coords=(0, 0)):
        self.__coords = coords   # приватный атрибут

    def get_coords(self):
        return self.__coords

    def set_coords(self, new_coords):
        self.__coords = new_coords

    def calculate_area(self):
        return 0  # базовый метод, переопределяется в дочерних

class Circle(Figure):
    def __init__(self, coords, radius):
        super().__init__(coords)
        self.radius = radius

    def calculate_area(self):
        return 3.14159 * self.radius ** 2

class Square(Figure):
    def __init__(self, coords, side):
        super().__init__(coords)
        self.side = side

    def calculate_area(self):
        return self.side ** 2

# Список фигур (5 штук)
figures = [
    Circle((0, 0), 3),
    Square((2, 1), 4),
    Circle((5, 5), 1.5),
    Square((0, 0), 2),
    Circle((1, 1), 2)
]

total_area = 0
for fig in figures:
    total_area += fig.calculate_area()

print(f"Общая площадь всех фигур: {total_area:.2f}")