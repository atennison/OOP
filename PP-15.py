myQueue =  []

def pushbook():
    myQueue.push(int(input("Enter the number you want to be in the queue: ")))

def dequeue():
   myQueue.pop(0)

def displayqueue():
    print(myQueue)

while True:
    print("1. Add to queue")
    print("2. Remove from queue")
    print("3. Print queue")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        pushbook()
    elif choice == 2:
       dequeue()
    elif choice == 3:
        displayqueue()
    elif choice == 4:
        break
