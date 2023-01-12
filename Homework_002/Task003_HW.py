# Реализуйте алгоритм перемешивания списка.
# НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, максимум использование библиотеки Random для и получения случайного int

import random
start_list = []
count = random.randint(5, 20)                       # задаем случаейное количество элементов списка от 5 до 20
for i in range(count):                              # заполняем список случайными числами от 0 до 99
       start_list.append(random.randint(0,99))
print(f'Start   list: {start_list}')                # вывод первоначального списка

for i in range(count):
    temp = start_list[i]
    x = random.randint(0, count-1)
    start_list[i] = start_list[x]
    start_list[x] = temp
print(f'Shuffle list: {start_list}')                # вывод перемешанного списка


# для наглядности с буквами
start_list = ['a', 'b', 'c', 'd', 'e']
print(f'Start   list: {start_list}')
for i in range(len(start_list)):
    temp = start_list[i]
    x = random.randint(0, len(start_list)-1)
    start_list[i] = start_list[x]
    start_list[x] = temp
print(f'Shuffle list: {start_list}')

#не в стиле C)))
import random
def create_list():
    my_list = []
    count = random.randint(5, 20)                       # задаем случаейное количество элементов списка от 5 до 20
    for i in range(count):                              # заполняем список случайными числами от 0 до 99
        my_list.append(random.randint(0,99))
    print(f'Start   list: {my_list}')
    return my_list                # вывод первоначального списка
def my_shuffle (my_list: list):
    ni = random.randint(0, len(my_list)-1)
    for i in range(len(my_list)):
        my_list[i], my_list[ni] = my_list[ni], my_list[i]
    print(f'Shuffle list: {my_list}')
    return my_list
my_list = create_list()
shuffled = my_shuffle(my_list)