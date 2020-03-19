"""<Функции для выравнивания и печати текста>"""

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


