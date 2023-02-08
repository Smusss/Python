import menu
contact_list = []
path = r'Practice_007\contact_list.txt'


def open_contact_list():  # 2: Открыть файл
    global contact_list
    contact_list = []  # иначе начинает дублировать запись при повторном выводе
    global path
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
        for line in data:
            contact_list.append(line.strip().split(';'))
    return contact_list


def get_contact_list():
    global contact_list
    return contact_list


def update_contact_list(contact):
    global contact_list
    contact_list.append(contact)
    return contact_list


def save_contact_list():  # 3: Сохранить файл
    global contact_list
    global path
    data = ''
    for item in contact_list:
        data += item[0] + ';' + item[1] + ';' + item[2] + '\n'
    with open(path, 'w', encoding='UTF-8') as file:
        data = file.write(''.join(data))


def find_contact(contact_info: str):  # 7: Найти контакт
    global contact_list
    result = []
    for item in contact_list:
        for field in item:
            if contact_info in field:
                result.append(item)
                print(f'Found contact: {item[0]} {item[1]} ({item[2]})')
                # break
    return result


def check_exit():  # 8: Выйти из программы
    global contact_list
    global path
    fix_list = []
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
        for line in data:
            fix_list.append(line.strip().split(';'))
    result = 0
    if fix_list != contact_list:
        result = 1
    return result


def delete_contact(contact: list):  # 6: Удалить контакт
    global contact_list
    if contact != []:
        for i in range(len(contact_list)):
            for item in contact:
                if contact_list[i] == item:
                    contact_list.pop(i)
    return contact_list


def change_contact(changing: list, changes: list):  # 5: Изменить контакт
    global contact_list
    for item in contact_list:
        for chg in changing:
            if item == chg:
                for i in range(len(menu.contact_structure)):
                    if changes[i] != '':
                        item[i] = changes[i]
    return contact_list
