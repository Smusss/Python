#Напишите программу вычисления арифметического выражения заданного строкой. 
# Используйте операции +,-,/,*. приоритет операций стандартный.
#*Пример:* 2+2 => 4; 1+2*3 => 7; 1-2*3 => -5;

#my_str = input('Input operations:')
my_str = '2+8-5*2-10/5'
def operations(list, symb):
    while symb in list:
        i = list.index(symb)
        if symb == '^':
            list[i-1] = float(list[i-1]) ** float(list[i+1])
        if symb == '*':
            list[i-1] = float(list[i-1]) * float(list[i+1])
        if symb == '/':
            list[i-1] = float(list[i-1]) / float(list[i+1])
        if symb == '+':
            list[i-1] = float(list[i-1]) + float(list[i+1])
        if symb == '-':
            list[i-1] = float(list[i-1]) - float(list[i+1])
        list.pop(i)
        list.pop(i)
    return list

new_str = my_str.replace(' ','').replace('+',' + ').replace('-',' - ').replace('*',' * ').replace('/',' / ').split()
print(new_str)
symb = '^'
new_str = operations(new_str, symb)
symb = '*'
new_str = operations(new_str, symb)
symb = '/'
new_str = operations(new_str, symb)
symb = '+'
new_str = operations(new_str, symb)
symb = '-'
new_str = operations(new_str, symb)
print(new_str)