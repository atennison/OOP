# storaging things as *.txt which is text storage
#*.dat #object
#MYSQL Database

#storage in text file
file1 = open("mytext.txt", "a")
file1.writelines(input("Enter your name: "))
file1.writelines(" This is Monday ")
file1.writelines(" How are you?")
file1.close()

file2 = open("mytext.txt", "r")
for line in file2:
    print(line)
file2.close()