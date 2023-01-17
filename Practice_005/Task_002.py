# Дан список чисел. Создайте список, в который попадают числа, описываемые возрастающую последовательность.
# Порядок элементов менять нельзя.

import random
my_list = [i for i in range(20)]
random.shuffle(my_list)
print(my_list)
for i in range(len(my_list)):
    temp = my_list[i]
    new_list = [temp]
    for j in range(i + 1, len(my_list)):
        if temp + 1 == my_list[j]:
            new_list.append(my_list[j])
            temp += 1
    if len(new_list) >= 2:
        print(new_list)