# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример: если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# Расширить значение коэффициентов до [-100..100]

#VERSION 1 - LIST
import random
k = int(input('Введите спепень = '))
if k == 0:
   print('Нулевая степень')
else:
    coeff = []
    for i in range(k+1):
        coeff.append(random.randint(-100,100))
    print(coeff)
    my_string = ' '
    for i in range(k+1):
        if coeff[i] != 0:
            new_str = ' + ' + str(coeff[i])
            if i == len(coeff) - 2:
                new_str += '*x'
            elif i != len(coeff) - 1:
                new_str += '*x**' + str(len(coeff)-1 -i)
            my_string += new_str
    result = my_string.replace('+ -','-').replace('-','- ').replace(' 1*x',' x').replace('  +', '') + ' = 0'
    print(result)

#VERSION 2 - DICTIONARY
import random
k = int(input('Введите спепень = '))
if k == 0:
   print('Нулевая степень')
else:
    dict = {}
    for i in range(k, -1, -1):
        dict[i] = random.randint(-100,100)
print(dict)
my_string = ''
for key, value in dict.items():
    if value != 0:
        new_str = ' + ' + str(dict[key])
        if key == 0:
            new_str += ' = 0'
        elif key == 1:
            new_str += '*x'
        else:
            new_str += '*x**' + str(key)
        my_string += new_str
result = my_string.replace('+ -','- ').replace(' 1*x', ' x')
if result.startswith(' + '):
    result = result[3:(len(my_string))]
print(result)