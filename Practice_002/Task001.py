# Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
# Пример: Для N = 5: 1, -3, 9, -27, 81

number = int(input('Введите число N: '))
my_list = [1]
for i in range(1, number):
    my_list.append(my_list[i-1] * -3)
print(*my_list)

number = int(input('Введите число N: '))
print(f"N = {number}:", end=" ")
for i in range(number):
    print((-3)**i, end=", ")

number = int(input('Введите число N: '))
my_list = []
for i in range(number):
    my_list.append((-3)**i)
print(f"N = {number}:", end=" ")
print(*my_list, sep=", ")