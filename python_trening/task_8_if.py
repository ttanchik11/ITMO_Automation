# num = -3
#
#
# if num >= 0:
#     print ('Число больше либо равно 0')
# else:
#     print('число отрицательное')

# str_2 содержит в себе str_1
#
# str_1 = 'test'
# str_2 = 'test1'
#
# def task_yes_no(str_1, str_2):
#     if str_1 in str_2:
#         print("ДА")
#     else:
#         print('НЕТ')
# task_yes_no(str_1='test', str_2='test2')
#
# num_float = 3.4
# if num_float > 0:
#         print("Положительное число")
# elif num_float == 0:
#         print('Ноль')
# else:
#     print("Число отрицательное")

# true = 1
# permit_print = True
#
# if num > 0 and permit_print:
#     print('num - положительное число')
# elif not permit_print:
#     print('Печать запрещена')


def student_rank(year_of_study):
    if year_of_study == 1 or year_of_study == 2 or year_of_study == 3 or year_of_study == 4:
        print('Бакалавр')
    elif year_of_study in range(5, 7):
        print('Аспирант')
    else:
        print('введите корректный год обучения')

student_rank(3)

def vasya(chislo):
   if chislo > 100 or chislo < -100:
        print("-")
   else:
        print("+")

vasya(30)