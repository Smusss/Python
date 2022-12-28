# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

number = input('Input number: ')
print(f'{number} ->', end=' ')
number = number.split(',')
#print(number)
sum = 0
for element in number:
    for num in element:
        sum = sum + int(num)
print(sum, end='. ')
print(f'Sum of elements = {sum}')
