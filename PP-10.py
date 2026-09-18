myCourses = {}
i= 1
while True:
    print("1. Add Course")
    print("2. Remove Course")
    print("3. Replace Course")
    print("4. Print Course")
    print("5. Exit")
    choice = input("Enter your choice:")
    if choice == 1:
        course_name = input("Enter your course name:")
        myCourses.update({"c_name" + str(i): course_name})
        i = i + 1
    elif choice == 2:
        del myCourses["c_name"]
    elif choice == 3:
        myCourses["c_name"] = (input("Enter your course name: "))
    elif choice == 4:
        print(myCourses)
    elif choice == 5:
        break
