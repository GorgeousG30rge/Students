from Visitor import VisitorUnderperform
from Visitor import VisitorExcellent
from Visitor import Visitor
from StudentsClass import StudentsRepository
from StudentsClass import *
from Decorate import DecorateTotal
from Decorate import DecorateUnderperform
from Decorate import DecorateExcellent
from Decorate import DecorateChanges


def create_main_menu():
    return Menu.create_menu('Главное меню', [
        DecorateTotal(Command('Показать всех студентов', print_all_students)),
        DecorateUnderperform(Command('Показать неуспевающих', print_underperforming_students)),
        DecorateExcellent(Command('Показать отличников', print_excellent_students)),
        DecorateChanges(Command('Добавить студента', create_student)),
        DecorateChanges(Command('Изменить студента', change_student)),
        DecorateChanges(Command('Удалить студента', delete_student))
    ])


def print_all_students():
    print('Список всех студентов')
    table_print(header)
    visit_all = Visitor()
    repository.accept(visit_all)

    print('#' * 141)


def print_underperforming_students():
    print('Список отстающих студентов')
    table_print(header)
    visit_underperforming_students = VisitorUnderperform()
    repository.accept(visit_underperforming_students)

    print('#' * 141)


def print_excellent_students():
    print('Список отличников')
    table_print(header)
    visit_excellent_students = VisitorExcellent()
    repository.accept(visit_excellent_students)

    print('#' * 141)


def create_student():
    LastName = input('Введите фамилию студента: ')
    FirstName = input('Введите имя студента: ')
    PatronymicName = input('Введите отчество студента: ')
    Group = input('Введите группу студента: ')
    student_x = Student(LastName, FirstName, PatronymicName, Group)
    repository.addStudent(student_x)



def change_student():
    print_all_students()
    student_index = int(input('Введите номер студента: '))

    Sub_Menu = Menu.create_menu('Изменить студента', [
        DecorateChanges(Command('Изменить имя', change_student_name, [student_index])),
        DecorateChanges(Command('Добавить оценки', add_marks, [student_index])),
    ])
    Sub_Menu.execute()



def change_student_name(student_index):
    LastName = input('Введите фамилию студента: ')
    FirstName = input('Введите имя студента: ')
    PatronymicName = input('Введите отчество студента: ')
    Group = input('Введите группу студента: ')

    repository.getStudent(student_index).FirstName = FirstName
    repository.getStudent(student_index).LastName = LastName
    repository.getStudent(student_index).PatronymicName = PatronymicName
    repository.getStudent(student_index).Group = Group



def add_marks(student_index):
    print_all_students()
    sub = input('Введите предмет: ')
    mark = int(input('Введите оценку: '))
    repository.getStudent(student_index).Marks[sub] = mark



def delete_student():
    print_all_students()
    remove = int(input('Введите номер студента, которого следует удалить из списка: '))
    repository.remove_student(remove)



header = ['Номер', 'Фамилия', 'Имя', 'Отчество', 'Группа']
def table_text(text, length):
    if len(text) > length:
        text = text[:length]
    elif len(text) < length:
        text = (text + " " * length)[:length]
    return text


def table_print(row):
    print('#' * 141)
    print('#', end=' ')
    for col in row:
        print(table_text(str(col), 25), end=' # ')
    print()

