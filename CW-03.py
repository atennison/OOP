class Faculty:
    def __init__(self):
            self.id = ""
            self.name = ""
            self.department = ""
            self.students = []
    def create_new_faculty(self):
            self.id = input("Enter faculty ID: ")
            self.name = input("Enter name: ")
            self.department = input("Enter department: ")
    def display_faculty(self):
            print("ID: " + self.id)
            print("Name: " + self.name)
            print("Department: " + self.department)

    def enrolled_student(self):
            self.students.append(student)
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
        self.advisor = faculty_id
        faculty.enroll_students(self)
class Course:
    def __init__(self):
        self.number = ""
        self.name = ""
        self.department = ""
        self.faculty_id = ""
        self.students = []
    def create_new_course(self):
        self.number = input("Enter course number: ")
        self.name = input("Enter name: ")
        self.department = input("Enter department: ")
    def display_course(self):
        print("Number: " + self.number)
        print("Name: " + self.name)
        print("Department: " + self.department)
    def assign_faculty(self):
        self.faculty = faculty_id
    def register_student(self):
        self.students.append(student)
myStudentList = []
myFacultyList = []
myCourseList = []
fac= Faculty()
fac.create_new_faculty()
myFacultyList.append(fac)

stu= Student()
stu.create_new_student()

faculty_id = input("Enter faculty ID: ")
for x in myFacultyList:
    if x.id == faculty_id:
        stu.assign_advisor(x)
myStudentList.append(stu)
cou = Course()
cou.create_new_course()
cou.assign_faculty(faculty_id)
myCourseList.append(cou)


