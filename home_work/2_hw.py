# def task_1():
#     my_int = 42
#     my_float = 3.14
#     my_str = "Hello, Python!"
#     my_list = [1, 2, 3, 4]
#     my_bool = True
#
#     print(f'Type of my_int: {type(my_int)}')
#     print(f'Type of my_float: {type(my_float)}')
#     print(f'Type of my_str: {type(my_str)}')
#     print(f'Type of my_list: {type(my_list)}')
#     print(f'Type of my_bool: {type(my_bool)}')
#
# # Вызов функции
# task_1()

#
# def task_2():
#     a = [1, 2, 3, 5, 8, 13, 21]
#     print(a[:3])
# task_2()

#задание 2
def find_maximum(num1, num2):
    maximum = max(num1, num2)
    print("Наибольшее число:", maximum)

find_maximum(10, 20)
find_maximum(-5, 3)
find_maximum(7.5, 2.5)

#задание 3
def difference(num1, num2):
    if abs(num1 -  num2) == 135:
        print("да")
    esle:(
        print("нет"))

# Пример вызова функции
difference(10, 145)

#задание 4
def season(month):
    if month == 1 or month == 2 or month == 12:
        print('зима')
    if month == 3 or month == 4 or month == 5:
        print('весна')
    if month == 6 or month == 7 or month == 8:
        print('лето')
    if month == 9 or month == 10 or month == 11:
        print('осень')

season(5)

#задание 5
def cisla_10(num1, num2, num3):
    if num1 > 10 and num2 > 10 and num3 >10:
        print('yes')
    else:
        print('no')

cisla_10(1,2,9)