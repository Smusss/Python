from random import randint as RI
my_list = [RI(0,10) for i in range(RI(1,10))]
new_len = int(len(my_list) / 2)
if len(my_list) % 2 != 0:
    new_len += 1
new_list = [my_list[i] * my_list[len(my_list)- 1 - i] for i in range(new_len)]
print(f'{my_list} => {new_list}')

# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16];  [2, 3, 5, 6] => [12, 15]
'''
import random
my_list = []
for i in range(random.randint(1,10)):
    my_list.append(random.randint(0,10))
if len(my_list) % 2 == 0:
    new_len = int(len(my_list) / 2)
else:
    new_len = int(len(my_list) / 2 + 1)
new_list = []
for i in range(new_len):
    new_list.append(my_list[i] * my_list[len(my_list)- 1 - i])
print(f'{my_list} => {new_list}')
'''