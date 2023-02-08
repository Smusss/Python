import menu


def show_menu():
    print(menu.command_menu)


def input_command():
    while True:
        try:
            user_input = int(input('\nInput menu item number: '))
            if 1 <= user_input <= 8:
                return user_input
            else:
                print('Нет такой команды!')
        except:
            print('Uncorrect input. Try again')


def show_all_contacts(contacts: list):  # 1: Показать все контакты
    if len(contacts) > 0:
        print('YOUR PHONE BOOK:')
        for item in contacts:
            print(f'{item[0]} {item[1]} ({item[2]})')
    else:
        print('Contact list is empty')


def load_successeful():  # 2: Открыть файл
    print("Contact list loaded successeful.")


def save_successeful():  # 3: Сохранить файл
    print("Contact list saved successeful.")


def input_new():  # 4: Новый контакт
    new = []
    for item in menu.contact_structure:
        new.append(input(f'Введите значение графы "{item}": '))
    return new


def search_contact():
    search = input('Input information about contact: ')
    return search


def search_result(find_result: list):
    if find_result == []:
        print('There is no same contact in your phone book.')


def end_work():
    print('\n*** WORK FINISHED ***\n')


def delete_successeful(info: list):  # 6: Удалить контакт
    if info != []:
        print("Contact deleted successeful.")


def check_exit_result(result):
    end_command = 8
    if result == 1:
        print('There is NO SAVED information!!!')
        while True:
            try:
                end_command = int(
                    input("\nFor save press 3, for exit press 8: "))
                if end_command == 8 or end_command == 3:
                    return end_command
                else:
                    print('There is not same command. Save (3) or Exit(8)?')
            except:
                print('Uncorrect input. Try again')
    return end_command


def input_changes(changing_contact):
    changes = []
    if len(changing_contact) > 1:
        print('\nMore then one contact for change!!! Choose ONE.')
    elif changing_contact != []:
        print('\nInput changes in the fields. If there is not changes in a field - press Enter:')
        c = ''
        for i in range(len(menu.contact_structure)):
            c = input(
                f'Change field "{menu.contact_structure[i]}" (old value: {changing_contact[0][i]}): ')
            if c is None:
                c = ''
            changes.append(c)
    return changes


def change_successeful(changing_contact, changes):  # 5: Изменить контакт
    if changing_contact == [] or changes == []:
        print("Nothing to change.")
    else:
        print("Contact list changed successeful.")
