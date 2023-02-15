import data_school


def input_class():  # 1. Какой класс?
    print('Выберите класс:')
    for i, item in enumerate(data_school.school_classes):
        print(f'{i+1}. {item}')
    while True:
        try:
            inp_class = int(input('Введите номер класса по порядку: '))
            count = 0
            for i, item in enumerate(data_school.school_classes):
                if (inp_class - 1) == i:
                    inp_class = item
                    count = 1
                    break
            if count == 1:
                return inp_class
            else:
                print('Нет такого класса!')
                # break
        except:
            print('Uncorrect input. Try again')


def show_class(cl):
    print(f'Вы выбрали {cl} класс.\n')


def input_subject():  # 2. Какой предмет?
    print('Выберите предмет:')
    for i, item in enumerate(data_school.subjects):
        print(f'{i+1}. {item}')
    while True:
        try:
            inp_sub = int(input('Введите номер предмета по порядку: '))
            count = 0
            for i, item in enumerate(data_school.subjects):
                if (inp_sub - 1) == i:
                    inp_sub = item
                    count = 1
                    break
            if count == 1:
                return inp_sub
            else:
                print('Нет такого предмета!')
                # break
        except:
            print('Uncorrect input. Try again')


# 3. Показывает весь список учеников и их оценки по предмету
def show_children_grades(journal, school_class, subject):
    print(f'\nОценки учеников {school_class} класса по предмету "{subject}":')
    k = 1
    for item in journal:
        if item['class'] == school_class:
            print(f'{k}. {item["surname"]} {item["name"]}: {item[subject]}')
            k += 1


def input_victim(list, journal):  # 4. Вызвать к доске? если ввести exit то выходит из программы
    while True:
        try:
            inp_vict = int(input(
                '\nВыберите кто из вышеуказанного списка учеников (№) пойдет отвечать к доске или введите 0 для выхода из программы: '))
            if 0 < inp_vict <= len(list):
                victim = list[inp_vict - 1]
                print(
                    f'Вы вызвали к доске ученика: {journal[victim]["surname"]} {journal[victim]["name"]}.')
                return victim
            elif inp_vict == 0:
                print('Вы решили выйти из журнала.')
                victim = -1
                return victim
            else:
                print('Нет такого варианта!')
        except:
            print('Uncorrect input. Try again')


def input_grade():  # 5.На какую оценку ответ?
    while True:
        try:
            grade = int(input('\nОцените ответ ученика в баллах от 1 до 5: '))
            if 0 < grade <= 5:
                return grade
            else:
                print('Такой балл не предусмотрен оценочной системой.')
        except:
            print('Uncorrect input. Try again')


def update_journal_successeful():
    print('\nОценка за ответ ученика успешно внесена в журнал.')


def end_work():
    print('\n***END WORK***')


def show_all_journal(journal):
    print('\nПосмотреть полный журнал успеваемости учеников?')
    answer = input('Для просмотра введите "+", чтобы пропустить просмотр введите любой символ / число или нажмите Enter: ')
    if answer == '+':
        for item in journal:
            print(f"\n{item['surname']} {item['name']} - {item['class']} класс: ")
            for field in data_school.subjects:
                print(f'{field}: {item[field]};')