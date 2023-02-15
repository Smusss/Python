subjects = ['Math', 'Bio', 'Reading', 'Sport', 'Music']
school_classes = ['1A', '2Б', '3В']
journal_structure = ['surname', 'name', 'class',
                     'Math', 'Bio', 'Reading', 'Sport', 'Music']


'''
journal_structure = ['surname', 'name', 'class']

for item in subjects:
    journal_structure.append(item)
print (journal_structure)

['surname', 'name', 'class', 'Math', 'Bio', 'Reading', 'Sport', 'Music']

ЗАДАЧИ
1. Какой класс? открываем конкретный файл
2. Какой предмет?
    3. Показывает весь список учеников и их оценки по предмету
    4. Вызвать к доске? если ввести exit то выходит из программы
    5. На какую оценку ответ?
6. После выхода сохранить все изменения в текущий файл

Архитектура
school_children - список учеников в формате 'имя;фамилия;класс;оценки', файл .txt
data - формирование словаря из данных файла и справочников, файл .py
view - работа с пользователем, файл .py
main - основной файл запуска программы, файл .py
controller - основные операции, файл .py
model - основные операции с журналом, файл .py

структура списка словарей Журнал = [{'name': 'aaa',
                                    'surname': 'bbb',
                                    'class': '1a',
                                    'subject': [список оценок]
                                    ...}
                                    ///]

резервная копия данных:
Ivanov;Ivan;1A;2,3,4,5;3,3,3;4,3,2;4,4,4;5,2,1
Petrov;Petr;1A;5,5;2,3;4,4;5,4;4,2
Pugacheva;Alla;1A;2,3,4,5;3,3,3;4,3,2;4,4,4;5,2,2
Vasilev;Vasya;1A;2,3,4,5;3,3,3;4,3,2;4,4,4;5,2,3
Lady;Gaga;1A;2,3,4,5;3,3,3;4,3,2;4,4,4;5,2,5
Kirkorov;Phillip;2Б;2,3,4,5;3,3,3;4,3,2;4,4,4;5,2,4
Pitt;Bred;2Б;2,3,4,5;3,3,3;4,3,2;4,4,4;5,2,5
Huston;Whitney;2Б;2,3,4,5;3,3,3;4,3,2;4,4,4;5,2,5
Kerry;Jim;2Б;5,3,4,5;5,3,3;3,3,2;4,4,4;5,2,4
Depp;Johney;2Б;2,3,4,5;3,3,3;4,3,2;4,4,4;5,2,5
Poppins;Mary;3В;2,3,4,5;3,3,3;4,3,2;4,4,4;5,2,3
'''