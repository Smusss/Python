# Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.

N = input('Input number: ')
my_list = ['djfhg', 'hfuhke', '42jsdhgfg', 'kjshf42djb', 42]
for i in range(len(my_list)):
    if N in my_list[i]:
        print('Есть')
        break
else:
    print ('No')
