class Button:

    def __init__(self, text, link):
        self.text = text
        self.link = link

i = 1
while i <= 10:
    print(i)
    i += 1
    square = i ** 2  # Вычисляем квадрат числа
    print(f"Квадрат числа {i} равен {square}")


def sum_two_numbers(a, b):
        print(a + b)
        return a + b

sum_two_numbers(4, 5)

class Button:
        def __init__(self, text, link):
                self.text = text
                self.link = link

home = Button('Домой', '/home')
catalog_msk = Button('Каталог', '/msk/catalog')

#получаем доступ к атрибутам
print(home.text)
print('Кнопка ' + home.text + ' имеет ссылку ' + home.link)

print('\n')

print(catalog_msk.text)
print('Кнопка ' + catalog_msk.text + ' имеет ссылку ' + catalog_msk.link )

class ButtonTwo:
    def __init__(self, text, link, loc):
        self.text = text
        self.link = link
        self.loc = loc

    def click(self):
        return "Клик по локатору - {}".format(self.loc)
#создаем экземпляр класса
home_two = ButtonTwo('Домой', r'\home', 'button#home')

#вызываем метод
print(home_two.click())