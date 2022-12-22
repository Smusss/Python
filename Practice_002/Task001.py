# Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
# Пример: Для N = 5: 1, -3, 9, -27, 81

number = int(input('Введите число N: '))
my_list = [1]
for i in range(1, number):
    my_list.append(my_list[i-1] * -3)
print(*my_list)