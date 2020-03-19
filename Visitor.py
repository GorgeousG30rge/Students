
from PrintFs import table_print
from PrintFs import table_text

class Visitor:

    def visit(self, i, student):
        student_row = [
            i, student.LastName, student.FirstName, student.PatronymicName, student.Group
        ]
        table_print(student_row)


class VisitorUnderperform:
    def __init__(self, enableOutput = True):
        self.__counter = 0
        self.__enableOutput = enableOutput

    def count(self):
        self.__counter += 1

    def get_counter(self):
        return self.__counter 

    def visit(self, i, student):
        student_row = [
            i, student.LastName, student.FirstName, student.PatronymicName, student.Group,
        ]
        underperform = False
        for s in student.Marks:
            if student.Marks[s] == 2:
                underperform = True
                
            if underperform:
                self.count()
                if self.__enableOutput:
                    table_print(student_row)
                break
            

class VisitorExcellent:
    def __init__(self, enableOutput = True):
        self.__counter = 0
        self.__enableOutput = enableOutput

    def count(self):
        self.__counter += 1

    def get_counter(self):
        return self.__counter 

    def visit(self, i, student):
        student_row = [
            i, student.LastName, student.FirstName, student.PatronymicName, student.Group,
        ]
        for s in student.Marks:
            excellent = True
            if student.Marks[s] != 5:
                excellent = False
                break
            if excellent:
                self.count()
                if self.__enableOutput:
                    table_print(student_row)
                break
