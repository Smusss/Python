# Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
# *Примеры:*
# - 6,78 -> 7
# - 5 -> нет
# - 0,34 -> 3

N = input('Input number: ')
count = 0
for i in N:
    if i == ',':
        break
    else:
        count += 1
if count == len(N):
    print('No decimal')
else:
    print(f'The first decimal place is {N[count+1]}')

M = float(input('Input number: '))
ost = (M * 10) % 10
if M - round(M) == 0:
    print('No')
else:
    print(round(ost))

M = float(input('Input number: '))
print(int(M * 10) % 10)

number = number.split(',')
print(number[1][0])