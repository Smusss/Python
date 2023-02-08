import view
import model


def start():
    view.show_menu()
    user_choise = 0
    while user_choise != 8:
        user_choise = view.input_command()
        match user_choise:
            case 1:
                contact_list = model.get_contact_list()
                view.show_all_contacts(contact_list)
            case 2:
                model.open_contact_list()
                view.load_successeful()
            case 3:
                model.save_contact_list()
                view.save_successeful()
            case 4:
                new_contact = view.input_new()
                model.update_contact_list(new_contact)
            case 5:
                info = view.search_contact()
                changing_contact = model.find_contact(info)
                changes = view.input_changes(changing_contact)
                if changing_contact != [] and changes != []:
                    model.change_contact(changing_contact, changes)
                view.change_successeful(changing_contact, changes)
            case 6:
                info = view.search_contact()
                search_result = model.find_contact(info)
                view.search_result(search_result)
                model.delete_contact(search_result)
                view.delete_successeful(search_result)
            case 7:
                info = view.search_contact()
                search_result = model.find_contact(info)
                view.search_result(search_result)
            case 0:
                view.show_menu()
    else:
        check_result = model.check_exit()
        end_command = view.check_exit_result(check_result)
        match end_command:
            case 3:
                model.save_contact_list()
                view.save_successeful()
                view.end_work()
            case 8:
                view.end_work()
