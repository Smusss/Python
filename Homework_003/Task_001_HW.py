# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на позиции с нечетным индексом.
# Пример: [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random
my_list = []
sum, positions = 0, ''
for i in range(random.randint(2,10)):
    my_list.append(random.randint(0,10))
    if i % 2 != 0:
        sum = sum + my_list[i]
        positions = positions + str(my_list[i]) + ', '
print(f'{my_list} -> на нечетных позициях элементы {positions}ответ: {sum}')
