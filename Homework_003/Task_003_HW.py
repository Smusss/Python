# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов, отличной от 0.
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random
max, min = 0.00, 1.00
my_list = []
for i in range(random.randint(1, 10)):
    my_list.append(round(random.uniform(0,10), 2))
    int_part = str(my_list[i]).split('.')[0]
    fract_part = my_list[i] - int(int_part)
    if fract_part !=0:
        if fract_part > max:
           max = fract_part
        if fract_part < min:
           min = fract_part
print(f'{my_list} => {round(max - min,2)} (max = {round(max,2)}, min = {round(min,2)})')