class Figure:
    def __init__(self, coords=(0, 0), width=1, color="black"):
        self.coords = coords
        self.width = width
        self.color = color

    def display(self):
        print(f"Фигура: координаты {self.coords}, ширина {self.width}, цвет {self.color}")

# Проверка
fig = Figure((5, 3), 2, "red")
fig.display()