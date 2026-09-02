# Задача 4 – Класс Graph

## Условие
Создайте класс `Graph`. Сделайте скрытыми его внутренние координаты `_x`, `_y` и `_scale`. Реализуйте методы:
- `move(dx, dy)` – перемещает график на заданные смещения;
- `change_scale(factor)` – изменяет масштаб.

Создайте три объекта `Graph`. Переместите первый, измените масштаб второго, третий оставьте в покое. Выведите их итоговое состояние.

## Решение
Атрибуты объявлены с одним подчёркиванием. Методы изменяют их значения. Для вывода состояния используется метод `display()` или прямой доступ через геттеры.

## Код
```python
class Graph:
    def __init__(self, x=0, y=0, scale=1.0):
        self._x = x
        self._y = y
        self._scale = scale

    def move(self, dx, dy):
        self._x += dx
        self._y += dy

    def change_scale(self, factor):
        self._scale *= factor

    def display(self):
        print(f"График: x={self._x}, y={self._y}, масштаб={self._scale}")

# Создание трёх графиков
g1 = Graph()
g2 = Graph(10, 5, 2.0)
g3 = Graph(-3, 7, 0.5)

# Действия
g1.move(5, -2)
g2.change_scale(1.5)

# Вывод состояния
g1.display()
g2.display()
g3.display()