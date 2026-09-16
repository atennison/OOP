mylist = []
index = 0
while True:
    print("1. Add Element to list")
    print("2. Remove Element from list")
    print("3. Replace an element from the List")
    print("4. Sort the elements in the List")
    print("5. Print List Elements")
    print("6. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        mylist.append(int(input("Enter a number to add to the list: ")))
        newlist = mylist[:]
        print(newlist)
    elif choice == 2:
        mylist.remove(int(input("Enter a number to remove: ")))
        newlist1 = mylist[:]
        print(newlist1)
    elif choice == 3:
     old_element=(int(input("Enter the number that you would like to delete: ")))
     new_element=(int(input("Enter the number that you would like to replace: ")))
     index = mylist.index(old_element)
     mylist[index] = new_element

    elif choice == 4:
        mylist.sort()
        newlist2 = mylist[:]
        print(newlist2)
    elif choice == 5:
        print(mylist)

    elif choice == 6:
        break



