import random
my_list = [random.randint(0,99) for i in range (random.randint(5, 20))]
my_shuffle_list = random.shuffle(my_list)
print(f'Start   list: {my_list}')
print(f'Shuffle list: {my_shuffle_list}')

# Реализуйте алгоритм перемешивания списка.
'''
import random
def create_list():
    my_list = []
    count = random.randint(5, 20)                       # задаем случаейное количество элементов списка от 5 до 20
    for i in range(count):                              # заполняем список случайными числами от 0 до 99
        my_list.append(random.randint(0,99))
    print(f'Start   list: {my_list}')
    return my_list                # вывод первоначального списка
def my_shuffle (my_list: list):
    ni = random.randint(0, len(my_list)-1)
    for i in range(len(my_list)):
        my_list[i], my_list[ni] = my_list[ni], my_list[i]
    print(f'Shuffle list: {my_list}')
    return my_list
my_list = create_list()
shuffled = my_shuffle(my_list)
'''