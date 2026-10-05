class Faculty:
    def __init__(self):
            self.id = ""
            self.name = ""
            self.department = ""
    def create_new_faculty(self):
            self.id = input("Enter faculty ID: ")
            self.name = input("Enter name: ")
            self.department = input("Enter department: ")
    def display_faculty(self):
            print("ID: " + self.id)
            print("Name: " + self.name)
            print("Department: " + self.department)

    def enrolled_student(self):

class Student:
    def __init__(self):
        self.id = ""
        self.name = ""
        self.department = ""
    def create_new_student(self):
        self.id = input("Enter student ID: ")
        self.name = input("Enter name: ")
        self.department = input("Enter department: ")
    def display_student(self):
        print("ID: " + self.id)
        print("Name: " + self.name)
        print("Department: " + self.department)
    def assign_advisor(self):
        self.advisor = input("Enter advisor: ")
class Course:
    def __init__(self):
        self.number = ""
        self.name = ""
        self.department = ""
    def create_new_course(self):
        self.number = input("Enter course number: ")
        self.name = input("Enter name: ")
        self.department = input("Enter department: ")
    def display_course(self):
        print("Number: " + self.number)
        print("Name: " + self.name)
        print("Department: " + self.department)
    def teaching_faculty(self):

    def enrolled_student(self):

myStudentList = []
myFacultyList = []
myCourseList = []


