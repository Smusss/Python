# Для натурального n создать словарь ключ-значение,состоящий из элементов последовательности 3n + 1.
# Пример: Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

my_dict = {}
n = int(input('Input number: '))
for i in range(1, n+1):
    my_dict[i] = 3*i + 1
print(f'Для n = {n}: {my_dict}')


my_dict = {}
n = int(input('Input number: '))
for key in range(1, n+1):
    my_dict[key] = 3*key + 1
print(f'Для n = {n}: {my_dict}')