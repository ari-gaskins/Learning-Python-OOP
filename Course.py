# part of student example

from Student import Student

class Course:

    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        # you can add attributes without them being set as parameters/arguments
        self.students = []

    def add_student(self, student):
        # if the amount of students is less than the maximum amount that can be added
        # add student passed in to the list, then return true if student is added successfully
        # return false if they are not able to be added
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def get_average_grade(self):
        pass
    
s1 = Student('Ari', 22, 95)
s2 = Student('Tom', 19, 75)
s3 = Student('Jill', 20, 65)