# Создайте программу для игры в 'Крестики-нолики'НЕОБЯЗАТЕЛЬНО Добавить игру против бота с интеллектом
import random

def make_battle_field_from_list(list):
    up = ' ___ ___ ___\n'
    down = '|___|___|___|\n'
    row = '|   |   |   |\n'
    battle_field = up + row
    for n in range(3):
        row_val = '| '
        for i in range(3*n, 3*n+3):
            if i == 2 or i == 5 or i == 8:
                row_val = row_val + str(list[i]) + ' |\n'
            else:
                row_val = row_val + str(list[i]) + ' | '
        if i == len(list) - 1:
            battle_field = battle_field + row_val + down
        else:
            battle_field = battle_field + row_val + down + row
    return battle_field

def check_pick(list):
    while True:
        try:
            pick = int(input("Input the number of field for you turn: "))
            if 0 < pick < 10:
                if pick not in list:
                    print('Field is busy, try again.')
                else:
                    return pick
            else:
                print('No such field, try again.')
        except:
            print('Uncorrect input, try again.')

def check_win (list):
    win = ''
    for i in range(1,len(list)-1,3):
        if list[i-1] == list [i] == list [i+1]:
            win = list[i]
    if list[2] == list [4] == list [6]\
        or list[0] == list [4] == list [8]:
        win = list[4]
    return win

field_list = [i+1 for i in range(9)]
battle_field = make_battle_field_from_list(field_list)                      #создание поля из списка
print(f'This is your battle field with numbers of fields: \n{battle_field}')
turn = random.randint(0, 1)                                                 #определение очередности хода и назначение Х и 0
if turn == 1:
    man, bot = 'X','0'
    print(f'\nLets go! You start! Your figure is "{man}".')
else:
    man, bot = '0', 'X'
    print(f'Lets go! Your Imaginary friend starts!\nYour figure is "{man}".')
turn = 'X'
for n in range(len(field_list)):                                            #поочередные ходы с выводом поля после каждого поля
    if turn == man:
        print(f'\nNext turn {man}! ({n+1})')
        pick_field = check_pick(field_list)
        for i in range(len(field_list)):
            if field_list[i] == pick_field:
                field_list[i] = man
                turn = bot
    else:                                                                   #TO DO заменить логику бота: 1 - 5, углы, 2+ и оборона,  2 - углы, оборона и 2+
        print(f'\nNext turn {bot}! ({n+1}) ')
        pick_field = check_pick(field_list)
        for i in range(len(field_list)):
            if field_list[i] == pick_field:
                field_list[i] = bot
                turn = man  
    print(make_battle_field_from_list(field_list))
    winner = check_win(field_list)
    if winner != '':
        break
if winner == man:
    print('YOU WIN!')
elif winner == bot:
    print('YOU LOSE(((')
else:
    print('Draw in the game><')