from tests.test_one import test_list

a=[5, 10, 15, 29, 25, 30, 25, 40]

#a(2)=15
print("a[2]=", a[2])

# a[0:3] = [5, 10, 15]
print("a[0:3]=", a[0:3])

#изменение элемента
b=[11,12,13]
b[2]=4
print(b)

test_list = ['один', 'два', 'три', 'четыре', 'пять']

for elem in test_list:
    print(elem)

print(len(test_list))

test_list.append('шесть')
print(test_list)