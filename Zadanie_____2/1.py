#Создать список и заполнить его элементами различных типов данных.
#Реализовать скрипт проверки типа данных каждого элемента. Использовать
#функцию type() для проверки типа. Элементы списка можно не запрашивать у
#пользователя, а указать явно, в программе

x1 = 5
Z = 1.2
str = "Строка"
list = ['a', '2']
tuple = ('b', '3')
set1 = {1, 2, 3, 4, 5, 6, 7, 8}
massive = [1, 2, 3, 4, 5, 'today', False]

vivod = [x1, Z, str, list, tuple, set1, massive]
for i in vivod:
    print(f'{i} is {type(i)}')