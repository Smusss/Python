import model
import view


def start():
    journal = model.open_journal()
    input_class = view.input_class()
    view.show_class(input_class)
    subject = view.input_subject()
    view.show_children_grades(journal, input_class, subject)
    vict_list = model.victim_list(journal, input_class)
    victim = view.input_victim(vict_list, journal)
    if victim != -1:
        grade = view.input_grade()
        model.update_grades(journal, victim, subject, grade)
        model.update_journal(journal)
        view.update_journal_successeful()
    view.show_all_journal(journal)
    view.end_work()
