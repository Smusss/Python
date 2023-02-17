from loader import dp, bot
from aiogram import types
import emoji
import random

game = False
sweets_bank = 0
max_take = 0
turn = 0
check = False

win = 'YOU WIN!!! All sweets are yours!\n'
lose = "YOU LOSE...I hope you don't like sweets.\n"

@dp.message_handler(commands=['start'])
async def mes_start(message:types.Message):
    print(message, emoji.emojize(':thumbs_up:', language = 'alias'))
    await message.answer("Hello! Let's play in my favourite game!\n"
                        "Press:\n"
                        "/YES for play\n"
                        "/RULES for show game rules\n"
                        "/NO if you are boring and busy person\n")

@dp.message_handler(commands=['RULES'])
async def mes_rules(message:types.Message):
    await message.answer(f'OOkkeeeyy!\n\n'
                         'Rules of the game:\n'
                         'On the table is the number of sweets that we will choose at the start.\n'
                         'Two players play by making moves one after the other.\n'
                         'The first move is determined by a draw.\n'
                         'In one move, you can collect no more than the maximum amount that we chose at the beginning.\n'
                         'Whoever makes the last move wins and takes all the candies.\n\n'
                         "Let's play, /YES?")

@dp.message_handler(commands=['YES'])
async def mes_yes(message:types.Message):
    global game
    global turn
    await message.answer("Let's get ready to rumble!\n"
                         "How many sweets are in the game?\n"
                         "Input /bank and a count of sweets ")
    game = True
    turn = random.randint(0, 1)
    return game, turn

@dp.message_handler(commands=['NO'])
async def mes_yes(message:types.Message):
    await message.answer("((((((((((((((((((")
    game = False
    return game

@dp.message_handler(commands=['bank'])
async def mes_set(message:types.Message):
    global sweets_bank
    count = message.text.split()[1]
    sweets_bank = int(count)
    await message.answer(f'Sweets bank = {sweets_bank}.\n'
                          "Input /max and count of max a count of sweets that can be taken by turn.")
    return sweets_bank

@dp.message_handler(commands=['max'])
async def mes_set(message:types.Message):
    global max_take
    count = message.text.split()[1]
    max_take = int(count)
    await message.answer(f'So, {max_take} sweets can be taken by turn.\n'
                          "Input /GO for start the game.")
    return max_take

@dp.message_handler(commands=['GO'])
async def mes_go(message:types.Message):
    global game
    global sweets_bank
    global max_take
    global turn
    if game is False:
        await bot.send_message(message.from_user.id, 'But you said that you do not want to play. \nTell me /YES, Bro)) ')
    elif sweets_bank <= 0:
        await bot.send_message(message.from_user.id, 'You did not set the count of sweets (sweets bank). \nTell me /set_bank and count!')
    elif max_take <= 1:
        await bot.send_message(message.from_user.id, 'You did not set the count of sweets can be taken by turn (max take). \nTell me /set_max and count!')
    else:
        if turn == 1:
            await bot.send_message(message.from_user.id, f'Your turn. There are {sweets_bank} sweets on the table. \nHow many sweets will you take?')
        else:
            take = sweets_bank % (max_take + 1)
            if sweets_bank <= max_take:
                take = sweets_bank
            elif take == 0:
                take = 1
                turn = 1
            sweets_bank = sweets_bank - take
            await bot.send_message(message.from_user.id, f'The Bot turn. He took {take} sweets.\n'
                                  f'There are {sweets_bank} on the table now.\n'
                                    'How many sweets will you take?')
        check = True
    return sweets_bank, turn, check
            
@dp.message_handler()
async def mes_all(message:types.Message):
    global win
    global lose
    global check
    global sweets_bank
    global max_take
    if check == True:
        if sweets_bank > 0:
            if message.text.isdigit():
                take = check_max_and_over(max_take, sweets_bank, message.text)
                sweets_bank -= take   
                await bot.send_message(message.from_user.id, f'You took {take} sweets, '
                                       f'there are {sweets_bank} sweets on the table now.')
                turn = 0
                if sweets_bank > 0:
                    take = sweets_bank % (max_take + 1)
                    if sweets_bank <= max_take:
                        take = sweets_bank
                    elif take == 0:
                        take = 1
                        turn = 1
                    sweets_bank = sweets_bank - take
                    await bot.send_message(message.from_user.id, f'The Bot turn. He took {take} sweets.\n'
                                                                f'There are {sweets_bank} on the table now.\n'
                                                                'How many sweets will you take?')
                else:
                    mess = judge(turn)
                    bot.send_message(message.from_user.id,mess)
            else:
                await bot.send_message(message.from_user.id, f'Input number.')
        else:
            mess = judge(turn)
            bot.send_message(message.from_user.id,mess)
    else:
        await message.answer(f"We cant't start the game(((\n"
                             'Press: */YES* and follow the line. I am waiting for you)))')

    def check_max_and_over(max, bank, mess):
        count = int(mess)
        if count <= max and count <= bank:
            return count
        else:
            if count > bank and count > max:
                 bot.send_message(message.from_user.id,(f'Over bank and over max. Try again! Bank is {bank}, max is {max}'))
            elif count <= max and count > bank:
                bot.send_message(message.from_user.id,(f'Over bank. Try again! Bank is {bank}'))
            else:
                bot.send_message(message.from_user.id,(f'Over max. Try again! Max is {max}'))

    def judge(turn):
        if turn == 0:
            result = 'YOU WIN!!! All sweets are yours!\n'
        else:
            result = "YOU LOSE...I hope you don't like sweets.\n"
        return result

@dp.message_handler(commands=['OOP'])
async def mes_oop(message:types.Message):
    await message.answer('What are you talking about?')

@dp.message_handler(commands=['Hi'])
async def mes_hi(message:types.Message):
    await message.answer(f'Hello, {message.from_user.first_name}! '
                         f'Long time no see!')

@dp.message_handler(text=['фу'])
async def mes_fu(message:types.Message):
    await bot.delete_message(message.from_user.id, message.message_id)
    await message.answer(f'Bad, bad, bad!')

'''
@dp.message_handler()   # если поставить его наверх - то он не пустит остальных и будет ловить все!
async def mes_all(message:types.Message):
    global total
    if message.text.isdigit():
        total-= int(message.text)
        await bot.send_message(message.from_user.id, f'конфет осталось {total}')
    else:
        await message.answer(f'Wow, look what i have got - {message.text}')
        '''