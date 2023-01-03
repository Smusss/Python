# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов, отличной от 0.
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random
max, min = 0.00, 1.00
my_list = []
for i in range(random.randint(1, 10)):
    my_list.append(round(random.uniform(0,10), 2))
    temp1 = str(my_list[i]).split('.')
    temp2 = my_list[i] - float(temp1[0])
    if temp2 !=0:
        if temp2 > max:
            max = temp2
        if temp2 < min:
            min = temp2
print(f'{my_list} => {round(max - min,2)} (max = {round(max,2)}, min = {round(min,2)})')