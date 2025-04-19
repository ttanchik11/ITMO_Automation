#задание 1

class Rectangle:
    def __init__(self, wight, length):
        self.wight = wight
        self.length = length
    def calc_square(self):
        return self.wight * self.length

    def calc_perimeter(self):
        return 2 * (self.wight + self.length)
p1 = Rectangle(1, 2)
p2 = Rectangle(4,6)
p3 = Rectangle(3,7)
print(f"Площадь1: {p1.calc_square()}")
print(f"Периметр1: {p1.calc_perimeter()}")
print(f"Площадь2: {p2.calc_square()}")
print(f"Периметр2: {p2.calc_perimeter()}")
print(f"Площадь3: {p3.calc_square()}")
print(f"Периметр3: {p3.calc_perimeter()}")

#задание 2

class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        result = self.a + self.b
        print(f"Сложение: {self.a} + {self.b} = {result}")
        return result

    def multiplication(self):
        result = self.a * self.b
        print(f"Умножение: {self.a} * {self.b} = {result}")
        return result

    def division(self):
        try:
            result = self.a / self.b
            print(f"Деление: {self.a} / {self.b} = {result}")
            return result
        except ZeroDivisionError:
            print(f"Ошибка: деление на ноль ({self.a}/{self.b})")
            return None

    def subtraction(self):
        result = self.a - self.b
        print(f"Вычитание: {self.a} - {self.b} = {result}")
        return result


calculator = Math(10, 5)

calculator.addition()
calculator.multiplication()
calculator.division()
calculator.subtraction()

zero_div = Math(10, 0)
zero_div.division()

#задание 3

class Sidebar:
    type: str = "Button"
    def __init__(self, text, loc=""):
        self.text = text
        self.loc = loc
    def click(self):
        return f"Клик по кнопке {self.text}"

buttons = [
    Sidebar("Text Box"),
    Sidebar("Check Box"),
    Sidebar("Radio Button"),
    Sidebar("Web Tables"),
    Sidebar("Buttons"),
    Sidebar("Links"),
    Sidebar("Broken Links - Images"),
    Sidebar("Upload and Download"),
    Sidebar("Dynamic Properties")
]
print("Текст кнопок:")
for button in buttons:
    print(f"- {button.text} (тип: {button.type})")
print("\n")

print("Результаты кликов:")
for button in buttons:
    print(button.click())