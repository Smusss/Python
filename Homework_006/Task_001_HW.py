# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
# 1 x > 0, y > 0 2 x < 0, y > 0 3 x < 0, y < 0 4 x > 0, y < 0

def quarter_number():
    dict = {1:'Диапазон координат: x > 0, y > 0.', \
            2:'Диапазон координат: x < 0, y > 0.', \
            3:'Диапазон координат: x < 0, y < 0.', \
            4:'Диапазон координат: x > 0, y < 0.'}
    while True:
        try:
            x = int(input('Введите номер четверти от 1 до 4: '))
            if x < 1 or x > 4:
                print('Uncorrect input')
            else:
                return str(dict[x])
        except:
            print('Uncorrect input (symbol)')
 
print(quarter_number())


#OLD VERSION
'''
try:
    a = int(input('Введите номер четверти от 1 до 4: '))
    if a < 1 or a > 4:
        print('Uncorrect input')
    else:
        if a == 1:
            print('Диапазон координат: x > 0, y > 0.')
        if a == 2:
            print('Диапазон координат: x < 0, y > 0.')
        if a == 3:
            print('Диапазон координат: x < 0, y < 0.')
        if a == 4:
            print('Диапазон координат: x > 0, y < 0.')
except:
    print('Uncorrect input (symbol)')
'''