#
# def add(x,y):
#     return x+y
#
# #вызываем функцию
# print(add(1,2))
#
#
# def arg(a, b, c=2, d=3):
#     return a+b+c+d
#
# print(arg(1, 1, 1, 1))
# print(arg(2,2))
# print(arg(2,2, 1))
#
# print(arg(2,2, '1',1))
#
#
# def range_arg(a, b, c, d):
#     return a + '' + b + '' + c + '' + d
#
# print(range_arg('1', '2', '3', '4'))
# print(range_arg('1', '2', d='3, c='4'))
#

#
# def add(x,y):
#     return x+y
#
# # #вызываем функцию
# print(add(1,2))
#

type(1>0)

# возведение в степень
5 ** 2
# 25 обратите внимание, что знак возведения не ^

# знак ^ относится к побитовым операциям
# и является побитовым ИСКЛЮЧАЮЩИМ ИЛИ (XOR), не путайте
5 ^ 2 # 7
# 5 = 101
# 2 = 010
# 101 ^ 010 = 111 = 7

def compute_surface(radius, pi = 3.14159):
    return pi*radius*radius
print (compute_surface(2))
