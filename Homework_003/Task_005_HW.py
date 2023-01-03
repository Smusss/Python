# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример: для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи

# Версия 1 с присоединением списков
import math
def input_number():
    while True:
        try:
            N = abs(int(input('Input number: ')))
            return N
        except:
            print('Uncorrect input')
N = input_number()
fibo = [0]
if N == 0:
    print(f'для k = {N} список будет выглядеть так: {fibo}')
else:
    fibo = [1, 0, 1]
    if N > 1:
        for i in range(N - 1):
            fibo.append(fibo[i+2] + fibo[i+1])
        for i in range(N - 1):
            temp = [fibo[1] - fibo[0]]
            temp.extend(fibo)
            fibo = temp
    print(f'для k = {N} список будет выглядеть так: {fibo}')

# Версия 2 с массивом заданной величины и заполнением по индексам
print('VERSION 2')
fibo = [0] * (N * 2 + 1)
if N == 0:
    print(f'для k = {N} список будет выглядеть так: {fibo}')
else:
    fibo [N - 1], fibo [N + 1]  = 1, 1
    for i in range(N + 1, N * 2):
        fibo[i + 1] = fibo[i - 1] + fibo[i]
    i = N - 2
    while i >= 0:
        fibo [i] = fibo[i + 2] - fibo [i + 1]
        i -= 1
    print(f'для k = {N} список будет выглядеть так: {fibo}')