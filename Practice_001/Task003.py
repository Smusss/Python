# Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
# *Примеры:*
# 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5

N = abs(int(input('Введите число N: ')))
i = 0
num = -N
while i < N*2+1:
    print(num)
    num += 1
    i += 1

N = abs(int(input('Введите число N: ')))
for i in range(-N, N+1):
    print(i)

N = abs(int(input('Введите число N: ')))
my_list = []
for i in range(-N, N+1):
    my_list.append(i)
print(my_list)

N = abs(int(input('Введите число N: ')))
my_str = ''
for i in range(-N, N+1):
    if i < N:
        my_str += str(i) + ', '
    else:
        my_str += str(i)
print(my_str)
