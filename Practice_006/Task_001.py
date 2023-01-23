# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
# *Пример:* [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

my_list = [1, 2, 3, 5, 1, 5, 3, 10]
print(my_list)
my_list = list(filter(lambda x: my_list.count(x) == 1, my_list))
print(my_list)

my_list = [1, 2, 3, 5, 1, 5, 3, 10]
print(my_list)
new_list = [x for x in my_list if my_list.count(x) == 1]
print(new_list)
