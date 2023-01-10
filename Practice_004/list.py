my_string = "Питон самый лучший язык в мире"

splitted = my_string.split(' ')
print(splitted)

replaced = my_string.replace(' ', '-')
replaced = my_string.replace('а', '').replace('и', 'Ы')
print(replaced)

down = my_string.lower()
print(down)
up = my_string.upper()
print(up)

if my_string.startswith('Пит'):
    print('Начинается!')
if my_string.endswith('ире'):
    print('...и не заканчивается!')

cuts = print(my_string[2:8])
dne = print(my_string[:: -1])

my_list = ['1', '2', '3', '4']
add = '-'
print(add.join(my_list))

new_string = 'khg+f=tyrduf48ygjhvjh6892jjgytyt'
num_list = []
letter_list = []
dot_list = []

for char in new_string:
    if char.isdigit():
        num_list.append(char)
    elif char in ['+', '=']:
         dot_list.append(char)
    else:
       letter_list.append(char)
print(new_string)
print(num_list)
print(letter_list)