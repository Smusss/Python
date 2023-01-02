# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

#x = int(input('Введите число x: '))
#y = int(input('Введите число y: '))
#z = int(input('Введите число z: '))

trigger = True
for x in [True, False]:
    for y in [True, False]:
        for z in [True, False]:
            if not(x or y or z) != (not x and not y and not z):
                print (f'При x = {x}, y = {y}, z = {z} выражение ложно')
                trigger = False
if trigger:
    print('Выражение всегда истинно')