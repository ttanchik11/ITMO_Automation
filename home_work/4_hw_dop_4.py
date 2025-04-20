# с классом Car.
# a. Создайте конструктор класса Car.
# b. Напишите пять методов.
# i. Первый — запуск автомобиля, при его вызове выводится сообщение «Автомобиль заведен».
# ii. Второй — отключение автомобиля — выводит сообщение «Автомобиль заглушен».
# iii. Третий — присвоение автомобилю года выпуска.
# Четвертый метод — присвоение автомобилю типа.
# iv. Пятый — присвоение автомобилю цвета.

class Car:
    def __init__(self, color=None, year=None, car_type=None):
        self.color = color
        self.year = year
        self.car_type = car_type


    def on_auto(self):
        print("Автомобиль заведен")
    def off_auto(self):
        print("Автомобиль заглушен")

    def set_year(self, year):
        self.year = year
        return f'год:{self.year}'

    def set_type(self, car_type):
        self.car_type = car_type
        return f'тип:{self.car_type}'

    def set_color(self, color):
        self.color = color
        return f'цвет:{self.color}'

auto1 = Car()
auto1.on_auto()
print(auto1.set_color("red"))
print(auto1.set_year(2020))
print(auto1.set_type("Седан"))
auto1.off_auto()