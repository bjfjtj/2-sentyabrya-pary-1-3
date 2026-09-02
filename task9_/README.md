# Задача 9 – Мини-графический редактор

## Условие
Создайте полноценную мини-систему, объединяющую три концепции ООП:

1. **Инкапсуляция**: Базовый класс `Figure` скрывает свои координаты (сделайте их приватными `__coords`). Доступ к ним только через методы `get_coords()` и `set_coords()`.
2. **Наследование**: Создайте классы `Circle` и `Square`, унаследованные от `Figure`.
3. **Полиморфизм**: В обоих дочерних классах реализуйте метод `calculate_area()`.

В главной программе создайте список из 5 разных фигур (круги и квадраты). В одном цикле посчитайте и выведите общую площадь всех фигур в списке.

## Решение
В базовом классе координаты хранятся в приватном атрибуте `__coords` (двойное подчёркивание). Доступ через геттер и сеттер. Классы `Circle` и `Square` переопределяют `calculate_area()`. В цикле для каждой фигуры вызывается `calculate_area()`, и площади суммируются.

## Код
```python
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