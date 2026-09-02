class Car:
    def __init__(self):
        self._engine_temperature = 20

    def start_engine(self):
        self._engine_temperature = 90
        print("Двигатель прогрет")

    def drive(self):
        if self._engine_temperature >= 90:
            print("Поехали!")
        else:
            print("Сначала прогрейте двигатель!")

# Создаём машину
my_car = Car()

# Попытка поехать без прогрева
my_car.drive()  # Сначала прогрейте двигатель!

# Прямой доступ к скрытому атрибуту (не рекомендуется)
print(f"Температура напрямую: {my_car._engine_temperature}")

# Прогрев
my_car.start_engine()
my_car.drive()  # Поехали!