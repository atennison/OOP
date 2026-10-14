import pickle


class Book:
    def __init__(self):
        self.title = ""
        self.author = ""
        self.book_id = ""
        self.publisher_year = ""
        self.publisher = ""
    def add_book(self):
        self.book_id = int(input("Enter book id: "))
        self.title = str(input("Enter title: "))
        self.author = str(input("Enter author: "))
        self.publisher = str(input("Enter publisher: "))
        self.publisher_year = int(input("Enter publisher year: "))
    def display_book(self):
        print(self.book_id)
        print(self.title)
        print(self.author)
        print(self.publisher)
        print(self.publisher_year)
class Author:
    def __init__(self):
        self.name = ""
        self.author_id = ""
        self.affiliation = ""
        self.country = ""
        self.phone = ""
        self.email = ""
    def add_author(self):
        self.name = str(input("Enter name: "))
        self.author_id = int(input("Enter author id: "))
        self.affiliation = str(input("Enter affiliation: "))
        self.country = str(input("Enter country: "))
        self.phone = str(input("Enter phone: "))
        self.email = str(input("Enter email: "))
    def display_author(self):
        print(self.name)
        print(self.author_id)
        print(self.affiliation)
        print(self.country)
        print(self.phone)
        print(self.email)
class User:
    def __init__(self):
        self.name = ""
        self.user_id = ""
        self.password = ""
        self.address = ""
        self.email = ""
        self.booksborrowed = []
    def add_user(self):
        self.name = str(input("Enter name: "))
        self.user_id = int(input("Enter user id: "))
        self.password = str(input("Enter password: "))
        self.address = str(input("Enter address: "))
        self.email = str(input("Enter email: "))
        self.booksborrowed.append(Book())
    def display_user(self):
        print(self.name)
        print(self.user_id)





while True:
    print("Choose an option")
    print("1. Add book")
    print("2. Display books")
    print("3. Add author")
    print("4. Display authors")
    print("5. Add user")
    print("6. Display users")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_book()
    elif choice == 2:
        display_book()
    elif choice == 3:
        add_author()
    elif choice == 4:
        display_author()
    elif choice == 5:
        add_user()
    elif choice == 6:
        display_user()
    elif choice == 7:
        break

BookList = []
AuthorList = []
UserList = []

B1 = Book()
B1.add_book()
book_file = open("BookList.dat", "ab")
pickle.dump(BookList, book_file)

A1 = Author()
A1.add_author()
author_file = open("AuthorList.dat", "ab")
pickle.dump(AuthorList, author_file)

U1 = User()
U1.add_user()
user_file = open("UserList.dat", "ab")
pickle.dump(UserList, user_file)
