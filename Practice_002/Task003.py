# Напишите программу, в которой пользователь будет задавать две строки, а программа - определять количество вхождений одной строки в другую.
text = 'Напишите программу, в которой пользователь будет задавать две строки,' \
       ' а программа - определять '\
       ' количество вхождений одной строки в другую.'
subtext = str(input('Введите букву:'))
count = 0
for i in range(len(text)):
      if  text [i] == subtext:
        count+=1
print(f'Количество вхождений буквы "{subtext}" в заданную строку равно {count}')

text = 'Напишите программу, в которой пользователь будет задавать две строки,' \
       ' а программа - определять '\
       ' количество вхождений одной строки в другую.'
print(text)
text = text.split() # при этом текст меняет тип со строки на список!!
print(text)
search = input('Input string:')
count = 0
for word in text:
    if search in word:
        count+=1
print(f'Количество вхождений строки "{search}" в заданную строку равно {count}')

text = "The world is not enough"
subtext = str(input('Input string:'))
text = text.split(subtext)
print(len(text) - 1)

text = 'Напишите программу, в которой пользователь будет задавать две строки,' \
       ' а программа - определять '\
       ' количество вхождений одной строки в другую.'
subtext = str(input('Введите текст:'))
count = 0
for i in range(len(text)):
      if  text[i : i + len(subtext)] == subtext:
        count+=1
print(f'Количество вхождений текста "{subtext}" в заданную строку равно {count}')