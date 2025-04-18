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