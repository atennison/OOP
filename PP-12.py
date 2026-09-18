students = {}
i=1
while True:
    print("1. Add Student")
    print("2. Remove Student")
    print("3. Edit Student")
    print("4. Print Student")
    print("5. Exit")
    choice = input("Enter your choice:")
    if choice == 1:
        name = input("Enter your name:")
        major = input("Enter your major:")
        year = input("Enter your year:")
        students.update({"name" + str(i): { "stu_name" : name, "stu_major" : major, "stu_year" : year }})
        i = i + 1
    elif choice == 2:
        del students[input("Student you want to delete:")]
    elif choice == 3:
        students[""] = input("Enter the name you want to replace")
        print(input('Enter the name you want to add'))
    elif choice == 4:
        print(students)
    elif choice == 5:
        break