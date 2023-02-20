from loader import dp, bot
from aiogram import types
import random
from dict import game_dict as gp
from dict import statistic_list as sl

win = 'YOU WIN!!! All sweets are yours!\n'
lose = "YOU LOSE...I hope you don't like sweets)))\n"

@dp.message_handler(commands=['start'])
async def mes_start(message:types.Message):
    global gp
    print(message)
    await message.answer("Hello! Let's play in my favourite game!\n"
                        "Press:\n"
                        "/YES for play\n"
                        "/RULES for show game rules\n"
                        "/NO if you are boring and busy person\n")
    gp[message.from_user.id] = {'game': False, 'sweets_bank': 0, 'max_take': 0, 'turn': 0, 'check': False, 'take': 0}

@dp.message_handler(commands=['RULES'])
async def mes_rules(message:types.Message):
    await message.answer(f'OOkkeeeyy, {message.from_user.first_name}!\n\n'
                         'Rules of the game:\n'
                         'On the table is the number of sweets that we will choose at the start.\n'
                         'Two players play by making moves one after the other.\n'
                         'The first move is determined by a draw.\n'
                         'In one move, you can collect no more than the maximum amount that we chose at the beginning.\n'
                         'Whoever makes the last move wins and takes all the candies.\n\n'
                         "Let's play, /YES?")

@dp.message_handler(commands=['YES'])
async def mes_yes(message:types.Message):
    global gp
    if gp [message.from_user.id] == {}: gp[message.from_user.id] = {'game': False, 'sweets_bank': 0, 'max_take': 0, 'turn': 0, 'check': False, 'take': 0}
    await message.answer("Let's get ready to rumble!\n"
                         "How many sweets are in the game?\n"
                         "Input /bank and a count of sweets ")
    gp[message.from_user.id]['game'] = True
    gp[message.from_user.id]['turn'] = random.randint(0, 1)

@dp.message_handler(commands=['NO'])
async def mes_yes(message:types.Message):
    await message.answer("((((((((((((((((((")
    gp[message.from_user.id]['game'] = False
    return gp

@dp.message_handler(commands=['bank'])
async def mes_set(message:types.Message):
    global gp
    if gp[message.from_user.id]['sweets_bank'] !=0: 
        await message.answer(f"Sweets bank is already full!\nThere are {gp[message.from_user.id]['sweets_bank']} sweets!")
    else:
        count = message.text.split()[1]
        gp[message.from_user.id]['sweets_bank'] = int(count)
        await message.answer(f'Sweets bank = {int(count)}.\n'
                            "Input /max and count of max a count of sweets that can be taken by turn.")
    #print (gp)
    return gp

@dp.message_handler(commands=['max'])
async def mes_set(message:types.Message):
    global gp
    if gp[message.from_user.id]['max_take'] !=0: 
        await message.answer(f"Decided!\nIt is {gp[message.from_user.id]['max_take']}!")
    else:
        count = message.text.split()[1]
        gp[message.from_user.id]['max_take'] = int(count)
        await message.answer(f'So, {int(count)} sweets can be taken by turn.\n'
                          "Input /GO for start the game.")
    #print(gp)
    return gp

@dp.message_handler(commands=['GO'])
async def mes_go(message:types.Message):
    global gp
    game_id = message.from_user.id
    if gp[game_id]['game'] is False:
        await bot.send_message(message.from_user.id, 'But you said that you do not want to play. \nTell me /YES, Bro)) ')
    elif gp[game_id]['sweets_bank'] <= 0:
        await bot.send_message(message.from_user.id, 'You did not set the count of sweets (sweets bank). \nTell me /bank and count!')
    elif gp[game_id]['max_take'] <= 1:
        await bot.send_message(message.from_user.id, 'You did not set the count of sweets can be taken by turn (max take). \nTell me /max and count!')
    else:
        gp[game_id]['check'] = True
        if gp[game_id]['turn'] == 1:
            await bot.send_message(message.from_user.id, f"Your turn. There are {gp[game_id]['sweets_bank']} sweets on the table. \nHow many sweets will you take?")
        else:
            bot_take = gp[game_id]['sweets_bank'] % (gp[game_id]['max_take'] + 1)
            if gp[game_id]['sweets_bank'] <= gp[game_id]['max_take']:
                bot_take = gp[game_id]['sweets_bank']
            elif bot_take == 0:
                gp[game_id]['take'] = 1
            gp[game_id]['turn'] = 1
            gp[game_id]['sweets_bank'] = gp[game_id]['sweets_bank'] - bot_take
            await bot.send_message(message.from_user.id, f'The Bot turn. He took {bot_take} sweets.\n'
                                  f"There are {gp[game_id]['sweets_bank']} on the table now.\n")
            if gp[game_id]['sweets_bank'] > 0:
                await bot.send_message(message.from_user.id, f'How many sweets will you take?')
            else:
                gp[game_id]['turn'] = 0
                mess = judge(gp[game_id]['turn'])
                await bot.send_message(message.from_user.id,mess)
                gp[game_id]['check'] = False
    #print(gp)
    return gp
            
@dp.message_handler()
async def mes_all(message:types.Message):
    global win
    global lose
    global gp
    game_id = message.from_user.id
    if gp[game_id]['check'] == True:
        gp[game_id]['turn'] = 1
        if message.text.isdigit():
            gp[game_id]['take'] = check_max_and_over(gp[game_id]['max_take'], gp[game_id]['sweets_bank'], message)
            gp[game_id]['sweets_bank'] = gp[game_id]['sweets_bank'] - gp[game_id]['take'] 
            await bot.send_message(message.from_user.id, f"You took {gp[game_id]['take']} sweets.\n"
                                    f"There are {gp[game_id]['sweets_bank']} sweets on the table now.")              
            if gp[game_id]['sweets_bank'] > 0:
                gp[game_id]['turn'] = 0
                bot_take = gp[game_id]['sweets_bank'] % (gp[game_id]['max_take'] + 1)
                if gp[game_id]['sweets_bank'] <= gp[game_id]['max_take']:
                    bot_take = gp[game_id]['sweets_bank']
                elif bot_take == 0:
                    bot_take = 1
                gp[game_id]['sweets_bank'] = gp[game_id]['sweets_bank'] - bot_take
                await bot.send_message(message.from_user.id, f'The Bot turn - he took {bot_take} sweets.\n'
                                                            f"There are {gp[game_id]['sweets_bank']} sweets on the table now.\n\n")
                if gp[game_id]['sweets_bank'] > 0:
                    await bot.send_message(message.from_user.id, 'How many sweets will you take?')
                else:
                    mess = judge(gp[game_id]['turn'])[0]
                    await bot.send_message(message.from_user.id,mess)
                    sl.append((game_id,judge(gp[game_id]['turn'])[1]))
                    gp.pop(game_id)
                    await bot.send_sticker(message.from_user.id,sticker=r'CAACAgIAAxkBAAEH1E5j86M9hMvDolOUjEtdmEGHZYtXIAACzQMAAu7UDQABtUV4nxtyAUkuBA')
            else:
                mess = judge(gp[game_id]['turn'])[0]
                await bot.send_message(message.from_user.id,mess)
                sl.append((game_id,judge(gp[game_id]['turn'])[1]))
                gp.pop(game_id)
                await bot.send_sticker(message.from_user.id,sticker=r'CAACAgIAAxkBAAEH1E5j86M9hMvDolOUjEtdmEGHZYtXIAACzQMAAu7UDQABtUV4nxtyAUkuBA')
        else:
            await bot.send_message(message.from_user.id, f'Input number.')      
    else:
        await message.answer(f"We cant't start the game(((\n"
                             'Press: /YES and follow the line. I am waiting for you)))')
    #print(gp)
    print(sl)
    
def check_max_and_over(max, bank, message:types.Message): # не реализован механизм проверки - в любом случае возвращается значение
    count = int(message.text)
    if count > bank and count > max:
        #bot.send_message(message.from_user.id,(f'Over bank and over max. Bank is {bank}, max is {max}, you  will take minimal of'))
        count = min(bank,max)
    if count <= max and count > bank:
        #bot.send_message(message.from_user.id,(f'Over bank. Bank is {bank} - i will help you - you will take all))'))
        count = bank
    if count > max and count <= bank:
        #bot.send_message(message.from_user.id,(f'Over max. Max is {max} - take it'))
        count = max
    return count

def judge(turn):
    if turn != 0:
        result = 'YOU WIN!!! All sweets are yours!\n'
        stat = 'winner'
    else:
        result = "YOU LOSE...I hope you don't like sweets.\n"
        stat = 'loser'
    return result, stat




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