# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
# Примеры:
# - 1, 4, 8, 7, 5 -> 8
# - 78, 55, 36, 90, 2 -> 90

number1 = int(input('Введите первое число: '))
number2 = int(input('Введите второе число: '))
number3 = int(input('Введите третье число: '))
number4 = int(input('Введите четвертое число: '))
number5 = int(input('Введите пятое число: '))
max = number1
if number2 > max:
    max = number2
if number3 > max:
    max = number3
if number4 > max:
    max = number4
if number5 > max:
    max = number5
print('max v.1 = ', max)

list = [0, 0, 0, 0, 0]
for i in range(len(list)):
    list[i] = int(input('Введите число № : '))
print(list)
max = list[0]
for i in range(len(list)):
    if list[i] > max:
        max = list[i]
print('max v.2 = ', max)

list = []
for i in range(5):
  list.append(int(input('Введите число № : ')))
print(list)
max = list[0]
for i in range(len(list)):
    if list[i] > max:
        max = list[i]
print('max v.3 = ', max)

number1 = int(input('Введите первое число: '))
number2 = int(input('Введите второе число: '))
number3 = int(input('Введите третье число: '))
number4 = int(input('Введите четвертое число: '))
number5 = int(input('Введите пятое число: '))
list = [number1, number2, number3, number4, number5]
max = list[0]
i = 0
while i < len(list):
    if list[i] > max:
        max = list[i]
    i+= 1
print('max v.4 = ', max)

number1 = int(input('Введите первое число: '))
number2 = int(input('Введите второе число: '))
number3 = int(input('Введите третье число: '))
number4 = int(input('Введите четвертое число: '))
number5 = int(input('Введите пятое число: '))
max = number1
for i in [number1, number2, number3, number4, number5]:
    if i > max:
        max = i
print('max v.5 = ', max)