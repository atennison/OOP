while (True):
    print("1 Addition")
    print("2 Subtraction")
    print("3 Multiplication")
    print("4 Division")
    print("5 Exit")
    choice = input("Enter your choice: ")
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    if choice == "1":
        c = a + b
        print(c)
    elif choice == "2":
        f= a - b
        print(f)
    elif choice == "3":
        k = a * b
        print(k)
    elif choice == "4":
        n = a / b
        print(n)
    elif choice == "5":
        exit()

