def create_list_with_rule():
    while True:
        try: 
            n = int(input('Input positive int n: '))
            if n < 0:
                print('Uncorrect input - negative')
            else:
                my_list = [i for i in range (1, n+1)]
                my_list = list(map(lambda x: round((1 + 1/x)**x,2), my_list))
                return my_list, n
        except:
            print('Uncorrect input (float, symbol and ect.)')

def sum_of_list_elements(list):
    sum = 0
    for i in list:
        sum = sum + i
    return sum

res_list = create_list_with_rule()[0]
print(f'Для n = {create_list_with_rule()[1]} -> {res_list}')
print(f'Сумма {sum_of_list_elements(res_list)}')



#OLD VERSION
# Задайте список из n чисел последовательности (1 + 1/n)**n, выведеите его на экран, а так же сумму элементов списка.
# Пример:
# Для n=4 -> [2, 2.25, 2.37, 2.44]
# Сумма 9.06
'''
try:
    n = int(input('Input positive int n: '))
    if n < 0:
        print('Uncorrect input - negative')
    else:
        my_list = []
        sum = 0
        for i in range(1, n + 1):
            my_list.append(round((1 + 1/i)**i,2))
            sum = sum + my_list[i-1]
        print(f'Для n = {n} -> {my_list}')
        print(f'Сумма {sum}')
except:
        print('Uncorrect input (float, symbol and ect.)')
'''