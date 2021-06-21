class Car():
    """Простая модель автомобиля"""

    def __init__(self, make, model, year):
        """Инициализация атрибута и описание автомобиля."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_read = 100

    def get_descriptive_name(self):
        """Возвращает аккуратно отформатированное описание."""
        long_name = (self.make.title() + " " + self.model.title() + " " + str(self.year) + " года")
        return long_name

    def read_odometer(self):
        """Выводит пробег машины в милях"""
        print("На этой машине пробег " + str(self.odometer_read) + " мили. ")

    def update_odometer(self, mileage):
        """Установить заданное значение на одометре.
        При попытке обратной прокрутки изменени отклоняются."""
        if mileage >= self.odometer_read:
            self.odometer_read = mileage
        else:
            print("Вы не можете скрутить одометр")

    def increment_odometer(self, miles):
        """Увеличивает показания одометра с заданным приращением."""
        self.odometer_read += miles

    def fill_gas_tank(self):
        """Обьём бензобака."""
        print("Обьём бензобака:" + " 120 литров")


class Battery():
    """Простая модель аккумулятора электромобиля."""

    def __init__(self, battery_size=70):
        """Инициализирует атрибуты аккумулятора"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Выводит информацию о мощности аккумулятора."""
        print("У этой машины есть " + "аккумулятор мощностью: " + str(self.battery_size) + "Кв/ч.")

    def get_range(self):
        """Выводит приблизительный запас хода для аккумулятора."""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = ("Эта машина может ехать примерно " + str(range))
        message += (" миль при полной зарядке.")
        print(message)

    def upgrade_battery(self):
        """Улучшение батареи."""
        if self.battery_size == 70:
            self.battery_size = 85
            print("Аккумулятор увеличен до 85 кВтч.")
        else:
            print("Аккумулятор уже обновлен.")


class ElectricCar(Car):
    """Представляет аспекты машины, специфические для электромобилей."""

    def __init__(self, make, model, year):
        """Инициализирует атрибуты класса-родителя.
        Затем инициализируем атрибуты, специфические для электромобиля."""
        super().__init__(make, model, year)
        self.battery = Battery()  # 4

    def fill_gas_tank(self):
        """У электромобиля нет бензобака."""
        print("Этой машине не нужен бензобак!")
