# Функции меню через Итератор
""""Iterator
def print_all_students():
    print('Список всех студентов')
    table_print(header)
    iterator = repository.new_iterator()
    while iterator.has_next():
        student = iterator.next()
        student_row = [
            iterator.get_iteration(), student.LastName, student.FirstName, student.PatronymicName, student.Group
        ]
        table_print(student_row)
    print('#' * 141)


def print_underperforming_students():
    print('Список отстающих студентов')
    table_print(header)
    iterator = repository.new_iterator()
    while iterator.has_next():
        student = iterator.next()
        student_row = [iterator.get_iteration(), student.LastName, student.FirstName, student.PatronymicName, student.Group]
        underperform = False
        for s in student.Marks:
            if student.Marks[s] == 2:
                underperform = True

            if underperform:
                table_print(student_row)
                break

    print('#' * 141)


def print_excellent_students():
    print('Список отличников')
    table_print(header)
    iterator = repository.new_iterator()
    while iterator.has_next():
        student = iterator.next()
        student_row = [
            iterator.get_iteration(), student.LastName, student.FirstName, student.PatronymicName, student.Group
        ]
        Excellent = True
        for s in student.Marks:
            if student.Marks[s] != 5:
                Excellent = False
                break

            if Excellent:
                table_print(student_row)
                break
    print('#' * 141)

Iterator"""
