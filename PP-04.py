

name = input("Enter your name: ")
course1 = int(input("Enter your course 1 score: "))
course2 = int(input("Enter your course 2 score: "))
course3 = int(input("Enter your course 3 score: "))
total = course1 + course2 + course3
percent = (total/300)*100
if percent <= 100 and percent >= 90:
    print("Grade A")
elif percent < 90 and percent >= 80:
    print("Grade B")
elif percent < 80 and percent >= 70:
    print("Grade C")
elif percent < 70 and percent >= 60:
    print("Grade D")
elif percent < 60 and percent >= 0:
    print("Grade F")