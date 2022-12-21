# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

try:
    x = int(input('Введите координату Х: '))
    y = int(input('Введите координату Y: '))
    if x == 0 and y == 0:
        print('Center')
    else:
        if x > 0:
            if y > 0:
                print('First (1)')
            elif y == 0:
                print('X line - right')
            else:
                print('Fourth (4)')
        elif x == 0:
            if y > 0:
                print('Y line - up')
            else:
                print('Y line - down')
        else:
            if y > 0:
                print('Second (2)')
            elif y == 0:
                print('X line - left')
            else:
                print('Third (3)')
except:
        print('Uncorrect input (symbol)')