# В файле находится N натуральных чисел, записанных через пробел.
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.

my_list = '1 2 3 4 6 10 11 13'
data = list(map(int, my_list.split()))
for i in range(1, len(data)):
    if data[i] - 1 != data[i - 1]:
        temp = data[i-1]+1
        print(f'Не хватает числа {temp}')