# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

def determine_day (number):
    try:
        number = int(number)
        if number == 6 or number == 7:
            print('YES! It is holiday, buddy!')
        elif number < 1 or number > 7:
            print('Uncorrect input')
        else:
            print('NO, it is weekday')
    except:
        print('Uncorrect input (symbol)')

number_of_day = input('Input number of a day (from 1 to 7): ')
determine_day(number_of_day)