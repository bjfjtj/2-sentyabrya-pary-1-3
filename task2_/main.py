class Cat:
    def __init__(self, breed, name, age):
        self.breed = breed
        self.name = name
        self.age = age

    def draw(self):
        print(f"На экране рисуется кот {self.name}, порода {self.breed}")

# Создание котов
cat1 = Cat("Сиамская", "Барсик", 3)
cat2 = Cat("Персидская", "Мурка", 5)
cat3 = Cat("Британская", "Том", 2)

# Вызов draw для каждого
cat1.draw()
cat2.draw()
cat3.draw()