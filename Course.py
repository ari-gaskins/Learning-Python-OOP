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
        # initializes value for average
        value = 0
        # for each student in the list of students for this course, add their grade to the given value
        for student in self.students:
            value += self.get_grade()
        # return the average grade, given the grades of the students in the course
        # and the number of students taking the course
        return value / len(self.students)

# creates student objects 
s1 = Student('Ari', 22, 95)
s2 = Student('Tom', 19, 75)
s3 = Student('Jill', 20, 65)

# creates course object
course = Course('Chemistry', 2)

# adds a student then prints the name of student added
course.add_student(s1)
print(course.students[0].name)
course.add_student(s2)
print(course.students[1].name)
# the following would return False because the max number of students have been reached
# course.add_ student(s3)