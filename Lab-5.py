import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="studentdb"
)
cursor = db.cursor()
class StudentMaster:
    def __init__(self, student_id, student_name, student_major, student_courses, student_cgpa):
        self.student_id = student_id
        self.student_name = student_name
        self.student_major = student_major
        self.student_courses = student_courses
        self.student_gpa = student_cgpa

class FacultyMaster:
    def __init__(self, faculty_id, faculty_name, faculty_department, faculty_courses):
        self.faculty_id = faculty_id
        self.faculty_name = faculty_name
        self.faculty_department = faculty_department
        self.faculty_courses = faculty_courses

students = [
    StudentMaster(1, "Andrew Tennison", "CS", ["OOP"], [4.0]),
    StudentMaster(2, "Wyatt Campbell", "Engineering ", ["Calculus 2"], [3.9]),
    StudentMaster(3, "Miles Bethell", "Business Management ", ["Business Calc"], [3.5]),
    StudentMaster(4, "Cole Gervias", "Nursing", ["Calc 3"], [4.2]),
    StudentMaster(5, "Ethan Bailey", "Secondary Ed", ["American Gov"], [3.7]),
]
faculty = [
    FacultyMaster(1, "Robby Hoegh", "History", ["Sociology"]),
    FacultyMaster(2, "Kcee Riechert", "Math", ["Calculus"]),
    FacultyMaster(3, "Nathan Roth", "History", ["American History"]),
    FacultyMaster(4, "Gina Green", "Business", ["Business Management"]),
    FacultyMaster(5, "Clayton McCullah", "Science", ["Biology"]),
]
def create_tables():
    cursor.execute("""
    CREATE TABLE Student IF NOT EXISTS StudentMaster(
    student_id INT PRIMARY KEY,
    student_name VARCHAR(50),
    student_major VARCHAR(50),
    student_courses VARCHAR(50),
    student_gpa
)
""")
    cursor.execute("""
    CREATE TABLE Faculty IF NOT EXISTS FacultyMaster(
    faculty_id INT PRIMARY KEY,
    faculty_name VARCHAR(50),
    faculty_major VARCHAR(50),
    faculty_courses VARCHAR(50),
)
""")
    db.commit()
    print("Student Tables Created")
def display_students():
    cursor.execute("SELECT * FROM Student")
    records = cursor.fetchall()
    for row in records:
        print("Student ID: ", row[0])
        print("Student Name: ", row[1])
        print("Student Major: ", row[2])
        print("Student Courses: ", row[3])
        print("Student GPA: ", row[4])
def display_faculty():
    cursor.execute("SELECT * FROM Faculty")
    records = cursor.fetchall()
    for row in records:
        print("Faculty ID: ", row[0])
        print("Faculty Name: ", row[1])
        print("Faculty Major: ", row[2])
        print("Faculty Courses: ", row[3])
while True:
    print("1. Create Tables")

    print("3. Display Students")
    print("4. Display Faculty")
    print("5. Display all Information")
    print("6. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        create_tables()
    elif choice == 3:
        display_students()
    elif choice == 4:
        display_faculty()
    elif choice == 6:
        break
    else:
        print("Invalid Choice")
cursor.close()
db.close()




