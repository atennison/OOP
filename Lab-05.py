import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="studentdb")
cursor = db.cursor()
class StudentMaster():
    def __init__(self, student_id, student_name, student_major, student_courses, student_cgpa):
        self.student_id = student_id
        self.student_name = student_name
        self.student_major = student_major
        self.student_courses = student_courses
        self.student_cgpa = student_cgpa
class FacultyMaster():
    def __init__(self, faculty_id, faculty_name, faculty_department, faculty_courses):
        self.faculty_id = faculty_id
        self.faculty_name = faculty_name
        self.faculty_department = faculty_department
        self.faculty_courses = faculty_courses
students =  [
    StudentMaster(1, "Andrew Tennison", "CS", "OOP", 4.0),
    StudentMaster(2, "Wyatt Campbell", "Engineering", "Calculus 2", 3.9),
    StudentMaster(3, "Miles Bethell", "Business Management", "Business Calc", 3.5),
    StudentMaster(4, "Cole Gervias", "Nursing", "Calc 3", 4.0),
    StudentMaster(5, "Ethan Bailey", "Secondary Ed", "American Gov", 3.7),
]
faculty = [
    FacultyMaster(1, "Robby Hoegh", "History", "Sociology"),
    FacultyMaster(2, "Kcee Riechert", "Math", "Calculus"),
    FacultyMaster(3, "Nathan Roth", "History", "American History"),
    FacultyMaster(4, "Gina Green", "Business", "Business Management"),
    FacultyMaster(5, "Clayton McCullah", "Science", "Biology"),
]
cursor.execute("""
    CREATE TABLE IF NOT EXISTS StudentMaster(
    StudentID INT PRIMARY KEY,
    Name Varchar(50),
    Major Varchar(50),
    Course Varchar(50),
    CGPA DECIMAL(10,2)
    )
""")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS FacultyMaster(
    FacultyID INT PRIMARY KEY,
    Name Varchar(50),
    Major Varchar(50),
    Course Varchar(50)
)
""")
db.commit()
print("Tables created successfully")
def insert_data():
    sql_s = "INSERT IGNORE INTO StudentMaster(StudentID, Name, Major, Courses, CGPA) VALUES (%s, %s, %s, %s, %s)"
    for s in students:
        cursor.execute(sql_s, (s.student_id, s.student_name, s.student_major, s.student_courses, s.student_cgpa))

    sql_f = "INSERT IGNORE INTO FacultyMaster( FacultyID, Name, Department, Courses) VALUES (%s, %s, %s, %s)"
    for f in faculty:
        cursor.execute(sql_f, (f.faculty_id, f.faculty_name, f.faculty_department, f.faculty_courses))
    db.commit()
    print("Tables created successfully")
def display_students():
    cursor.execute("SELECT * FROM StudentMaster")
    print("\n--- Students ---")
    for row in cursor.fetchall():
        print("StudentID: ", row[0])
        print("StudentName: ", row[1])
        print("StudentMajor: ", row[2])
        print("StudentCourses: ", row[3])
        print("StudentCgpa: ", row[4])

def display_faculty():
    cursor.execute("SELECT * FROM FacultyMaster")
    print("\n--- Faculty ---")
    for row in cursor.fetchall():
        print("FacultyID: ", row[0])
        print("FacultyName: ", row[1])
        print("FacultyMajor: ", row[2])
        print("FacultyCourses: ", row[3])
while True:
    print("\n--- Menu ---")
    print("1. Insert Data")
    print("2. Display Faculty")
    print("3. Display Students")
    print("4. Display All Information")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        insert_data()
    elif choice == 2:
        display_students()
    elif choice == 3:
        display_faculty()
    elif choice == 4:
        display_students()
        display_faculty()
    elif choice == 5:
        break
    else:
        print("Please enter a valid choice")
cursor.close()
db.close()
print("Database Closed")