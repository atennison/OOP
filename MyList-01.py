mylist = [2,3,4,5,6,7,8]

mylist.append(66) #adding an element to the list
mylist.remove(3) # remove an element
mylist.pop() #removes last element in list or whatever you put in the index
mylist.sort() # sorts in numerical order
newlist = mylist.copy()
newlist.append(60)

print(mylist)


for n in mylist:
    print(n)

newvalue = int(input())
if newvalue in mylist:
    print("element is in the list")
else:
    print("Element is not found")