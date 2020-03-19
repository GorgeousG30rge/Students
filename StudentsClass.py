import json

class Student:
    def __init__(self, LastName, FirstName, PatronymicName, Group):
        self.LastName = LastName
        self.FirstName = FirstName
        self.PatronymicName = PatronymicName
        self.Group = Group
        self.Marks = {}


class Iterator:
    def __init__(self, collection=[]):
        self.__iteration = -1
        self.__list = collection

    def get_iteration(self):
        # Используется для печати номера в таблице
        return self.__iteration

    def next(self):
        self.__iteration += 1
        return self.__list[self.__iteration]

    def has_next(self):
        return self.__iteration < len(self.__list) - 1


class StudentsRepository:
    @staticmethod
    def __new__(cls):
        if not hasattr(cls, '__instance'):
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        self.__students = []
        self.__FILE_NAME__ = 'data2.json'

    def new_iterator(self):
        it = Iterator(self.__students)
        return it

    def accept(self, visitor):
        for i in range(len(self.__students)):
            visitor.visit(i, self.__students[i])

    def studentsCount(self):
        return len(self.__students)

    def getStudent(self, index):
        return self.__students[index]

    def addStudent(self, student):
        self.__students.append(student)

    def remove_student(self, index):
        del self.__students[index]

    def SaveRepository(self):
        data = []
        for i in self.__students:
            studentData = {
                'LastName': i.LastName,
                'FirstName': i.FirstName,
                'PatronynicName': i.PatronymicName,
                'Group': i.Group,
                'Marks': i.Marks
            }
            data.append(studentData)

        with open(self.__FILE_NAME__, 'w') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def LoadRepository(self):

        with open(self.__FILE_NAME__, 'r') as f:

            data = json.load(f)

            for i in data:
                FirstName = i['FirstName']
                PatronymicName = i['PatronynicName']
                LastName = i['LastName']
                Group = i['Group']
                Marks = i['Marks']
                student = Student(LastName, FirstName, PatronymicName, Group)
                student.Marks = Marks
                self.__students.append(student)


class Command:
    def __init__(self, title, func, args=[]):
        self.__title = title
        self.__func = func
        self.__args = args
    
    def get_title(self):
        return self.__title

    def execute(self):
        self.__func(*self.__args)


class Menu(Command):
    def __init__(self, title):
        self.__commands_list = []
        Command.__init__(self, title, None)

    def commands_amount(self):
        return len(self.__commands_list)

    def check_commands(self):
        for command in self.__commands_list:
            print(command.get_title())

    def execute(self):
        isactive = True
        print(self.get_title())
        while isactive:
            for i in range(len(self.__commands_list)):
                print(i+1, '-', self.__commands_list[i].get_title())
            print(self.commands_amount()+1, '-', 'Назад')
            command = int(input('Введите команду из меню: '))
            if (self.commands_amount()+1) == command:
                break    
            else:
                self.__commands_list[command-1].execute()

    @staticmethod
    def create_menu(title, command_list):
        main_menu = Menu(title)
        main_menu.__commands_list = command_list
        return main_menu


repository = StudentsRepository()

repository.LoadRepository()

