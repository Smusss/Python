# B. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

import random
def create_polynomial(file_number):   # генерация случайного набора коэффициентов и формирование многочлена в виде строки и словаря (элементы и ключи - int)
    k = int(input(f'Введите степень многочлена из файла № {file_number}: ')) # не реализованы проверки на символ и < 0
    if k <= 0:
        print('Нулевая / отрицательная степень')
    else:
        dict = {}                               #создание словаря в соответствии с заданной степенью + 1 (свободный член, не умножаемый на х)
        for i in range(k, -1, -1):
            dict[i] = random.randint(-100,100)
    my_string = ''                              #создание строчки для набора многочлена по словарю
    for key, value in dict.items():
        if value != 0:
            new_str = ' + ' + str(dict[key])
            if key == 0:
                new_str += ' = 0'
            elif key == 1:
                new_str += '*x'
            else:
                new_str += '*x**' + str(key)
            my_string += new_str                    # прямая сборка строки
    result = my_string.replace('+ -','- ').replace(' 1*x', ' x')    # итоговое форматирование строки
    if result.startswith(' + '):
        result = result[3:(len(my_string))]
    print(f'Многочлен из файла № {file_number}:')
    print(result)
    return [result, dict]   #где-то в паралльленом мире берут не многочлен, а исходный словарь
def poly_to_dict(polynominal):        # формирование словаря из заданного многочлена (ключи = степени, элементы = коэфф)
    poly_for_dict = polynominal.replace(' ', '').replace('-', '+-').replace('*x**', '+').replace('*x', '+1').replace('=0', '').split('+')
    if (poly_for_dict[0] == ''):            #корректировка строки до набора чисел в формате чередования коэффициент-степень
        poly_for_dict.pop(0)
    if len(poly_for_dict) % 2 != 0:
        poly_for_dict.append(0)       #степень/ключ для свободного члена
    dict = {}
    for i in range(0, len(poly_for_dict) - 1, 2):
        dict[int(poly_for_dict[i+1])] = int(poly_for_dict[i])
    print(dict)
    return dict
def sum_of_dicts(dict1,dict2):        # сложение элементов словарей по ключам
    keys_list = set(list(dict1.keys()) + list(dict2.keys()))  #объединение ключей двух словарей, выборка уникальных через множество + сортировка?(Автоматом)
    dict_sum = {}                                             #создание словаря-суммы путем перебора ключей с проверкой на None
    for key in keys_list:
        if dict1.get(key) is None:
            dict_sum[key] = dict2.get(key)
        elif dict2.get(key) is None:
            dict_sum[key] = dict1.get(key)
        else:
            dict_sum[key] = dict1.get(key) + dict2.get(key)
    print(dict_sum)
    return dict_sum
def poly_from_dict(dictionary):       # формирование многочлена из словаря
    sum_poly = ''
    for key, value in dictionary.items():
        if value != 0:
            new_str = ' + ' + str(dictionary[key])
            if key == 0:
                new_str += ' = 0'
            elif key == 1:
                new_str += '*x'
            else:
                new_str += '*x**' + str(key)
            sum_poly = new_str + sum_poly               # обратная сборка строки
    result = sum_poly.replace('+ -','- ').replace(' 1*x', ' x')
    if result.startswith(' + '):
        result = result[3:(len(sum_poly))]
    print(result)

file_number = 1
poly1 = create_polynomial(file_number)[0]           # создание многочлена 1
file_number = 2
poly2 = create_polynomial(file_number)[0]           # создание многочлена 2      
print('Полученные словари:')                        # перевод многочленов в словари
dict1 = poly_to_dict(poly1)
dict2 = poly_to_dict(poly2)
print('Словарь, полученный суммированием элементов вышеуказанных словарей по ключам:')
dict_sum = sum_of_dicts(dict1,dict2)        # создание словаря-суммы
print('Сумма многочленов:')
poly_sum = poly_from_dict(dict_sum)      # перевод словаря в многочлен