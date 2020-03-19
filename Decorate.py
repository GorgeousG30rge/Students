from menu_commands import repository
from Visitor import *

class DecorateTotal:
    def __init__(self, comm):
        self.__comm = comm

    def get_title(self):
        count = repository.studentsCount()
        return self.__comm.get_title() + f' ({count})'
        #return self.__comm.get_title() + ' (' + count + ')'

    def execute(self):
        self.__comm.execute()


class DecorateExcellent(VisitorExcellent):

    def __init__(self, comm):
        VisitorExcellent.__init__(self)
        self.__comm = comm

    def get_title(self):
        visitor = VisitorExcellent(False) #Создаем новый экземпляр посетителя
        repository.accept(visitor)        # Прогоняем посетителя через базу студентов (репозиторий) 
        count = visitor.get_counter()
        return self.__comm.get_title() + f' ({count})'

    def execute(self):
        self.__comm.execute()


class DecorateUnderperform(VisitorUnderperform):
    def __init__(self, comm):
        VisitorUnderperform.__init__(self)
        self.__comm = comm

    def get_title(self):
        visitor = VisitorUnderperform(False)
        repository.accept(visitor)
        count = visitor.get_counter()
        return self.__comm.get_title() + f' ({count})'

    def execute(self):
        self.__comm.execute()


class DecorateChanges:
    def __init__(self, comm):
        self.__comm = comm

    def get_title(self):
        return self.__comm.get_title()
        #return self.__comm.get_title() + ' (' + count + ')'

    def execute(self):
        self.__comm.execute()
        repository.SaveRepository()
