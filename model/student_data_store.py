import json

class StudentDataStore:

    @staticmethod
    def getStudentsForTeacher(teacherID):
        students = []
        student = Student()
        student.name = 'Sup'
        student.age = 10
        student.language = 'Thai'
        student.locale = 'US'
        students.append(student)
        student.name = 'Manoj'
        student.age = 10
        student.language = 'Hindi'
        student.locale = 'US'
        students.append(student)
        return students

class Student:

    def __init__(self):
        self.name = ''
        self.age = 0
        self.language = ''
        self.locale = ''

    def to_dict(self):
        return {
            'name' : self.name,
            'age' : self.age,
            'language' : self.language,
            'locale' : self.locale
        }