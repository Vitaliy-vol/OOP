from abc import ABC, abstractmethod  # Для абстракції

# Абстракція: абстрактний клас Vehicle
class Vehicle(ABC):  # Наслідування: Vehicle — батьківський клас
    def __init__(self, brand):
        self._brand = brand  # Інкапсуляція: protected атрибут

    @abstractmethod  # Абстрактний метод, реалізація обов’язкова в підкласах
    def start_engine(self):
        pass

    def describe(self):
        print(f"Vehicle brand: {self._brand}")

# Наслідування: Car — підклас Vehicle
class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.__model = model  # Інкапсуляція: приватний атрибут

    def start_engine(self):  # Поліморфізм: різна реалізація методу start_engine
        print(f"{self._brand} {self.__model} engine started with a button.")

    def get_model(self):  # Геттер повертає значення приватного атрибута.
        return self.__model

    def set_model(self, model):  # Сеттер встановлює/змінює значення приватного атрибута
        self.__model = model

# Наслідування: Bike — підклас Vehicle
class Bike(Vehicle):
    def __init__(self, brand, bike_type):
        super().__init__(brand)
        self.__bike_type = bike_type  # Інкапсуляція: приватний атрибут

    def start_engine(self):  # Поліморфізм: інша реалізація того ж методу
        print(f"{self._brand} ({self.__bike_type}) bike started with a key.")

    def get_bike_type(self):
        return self.__bike_type

    def set_bike_type(self, bike_type):
        self.__bike_type = bike_type

        
class Tractor(Vehicle):
    def __init__(self, brand, weight):
        super().__init__(brand)
        self._weight = weight  # Інкапсуляція: приватний атрибут

    def start_engine(self):  # Поліморфізм: інша реалізація того ж методу
        print(f"{self._brand} ({self._weight}) bike started with a key.")

    def get_bike_type(self):
        return self._weight

    def set_bike_type(self, weight):
        self._weight = weight

# Колекція об'єктів різних підкласів
vehicles = [
    Car("Toyota", "Camry"),
    Bike("Yamaha", "Sport"),
    Car("BMW", "M8"),
    Bike("Harley-Davidson", "Cruiser"),
    Tractor("Claas", 2000)
]

# Поліморфізм: однаковий виклик для різних об'єктів
for v in vehicles:
    v.describe()
    v.start_engine()


# інкапсуляція це приховування внутрішньої структури об’єкта від зовнішніх впливів, дозволяє обмежити доступ до будь-якої функції у класі.
#Наслідування — це механізм, що дозволяє одному класу (підкласу або "дочірньому") 
# -успадкувати атрибути та методи іншого класу (базового або "батьківського").
#Поліморфізм — це здатність викликати один і той самий метод, але для різних типів об'єктів, які мають різну реалізацію цього методу.
#Абстракція — це приховування деталей реалізації та надання лише необхідного інтерфейсу для роботи.