# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит заданное количество конфет. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.
# a) Добавьте игру против бота
# b) Подумайте как наделить бота 'интеллектом'

import random

def check_input_number(message):
    while True:
        try:
            num = int(input(message))
            return num
        except:
            print('Uncorrect input')
def check_max_and_over(max, bank, count):
    while True:
        try:
            count = int(input(message))
            if count <= max and count <= bank:
                return count
            else:
                if count > bank and count > max:
                    print(f'Over bank and over max. Try again! Bank is {bank}, max is {max}')
                elif count <= max and count > bank:
                    print(f'Over bank. Try again! Bank is {bank}')
                else:
                    print(f'Over max. Try again! Max is {max}')
        except:
            print('Uncorrect input. Input number!')

print("Hello, sweety! It will be a great game!")
message = 'How many sweets are in the game? Bank: '
sweets_bank = check_input_number(message)
message = 'How many sweets can be taken by turn? Max: '
max_take = check_input_number(message)
if max_take >= sweets_bank:
    print('Wow, it will be the fastest game that i have seen)))')
turn, take = random.randint(0, 1), 0
if turn == 1:
    print('\nLets go! You start!')
else:
    print('Lets go! Your Imaginary friend starts!')
while sweets_bank > 0:
    if turn == 1:                                       # man's turn
        message = 'Your turn to take: '
        take = check_max_and_over(max_take, sweets_bank, message)
        turn = 0
        sweets_bank = sweets_bank - take
    else:                                               # comp's turn
        take = sweets_bank % (max_take + 1)
        if sweets_bank <= max_take:
            take = sweets_bank
        elif take == 0:
            take = 1
        print(f'Your Imaginary friend took sweets: {take}.')
        turn = 1
        sweets_bank = sweets_bank - take
    print(f'There are {sweets_bank} sweets in the bank.\n')
else:
    if turn == 0:
        print(f'YOU WIN!!! All sweets are yours!\n')
    else:
        print(f"YOU LOSE...I hope you don't like sweets.\n")