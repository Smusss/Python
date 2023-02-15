import data_school

path = r'Practice_008\school_children.txt'

def open_journal():
    short_list = []
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
        for line in data:
            short_list.append(line.strip().split(';'))
    for field in short_list:
        for i in range(len(field)):
            if ',' in field[i]:
                field[i] = field[i].split(',')
    journal = []
    for i in range(len(short_list)):
        temp = {}
        for j in range(len(data_school.journal_structure)):
            temp[data_school.journal_structure[j]] = short_list[i][j]
        journal.append(temp)
    # print(journal)
    return journal


def victim_list(journal, school_class):
    vict_list = []
    for i, item in enumerate(journal):
        if item['class'] == school_class:
            vict_list.append(i)
    return vict_list


def update_grades(journal, student, subject, grade):
    grade = str(grade)
    journal[student][subject].append(grade)


# 6. После выхода сохранить все изменения в текущий файл
def update_journal(journal):
    global path
    data = ''
    for item in journal:
        for field in data_school.journal_structure:
            data += str(item[field]) + ';'
        data = data[:len(data)-1] + '\n'
    #print(data)
    new_data = data.replace("'", '').replace('[', '').replace(']', '').replace(' ','')
    new_data = new_data[:len(new_data)-1]
    #print(new_data)
    with open(path, 'w', encoding='UTF-8') as file:
        new_data = file.write(new_data)
