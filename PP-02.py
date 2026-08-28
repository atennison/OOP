number1 = int(input("Enter Number 1: "))
number2 = int(input("Enter Number 2: "))
number3 = int(input("Enter Number 3: "))

if number1 > number2 and number1 > number3:
    print("Number 1 is the greatest number")
elif number2 > number1 and number2 > number3:
    print("Number 2 is the greatest number")
elif number3 > number1 and number3 > number2:
    print("Number 3 is the greatest number")

if number1 < number2 and number1 < number3:
    print("Number 1 is the smallest number")
elif number2 < number1 and number2 < number3:
    print("Number 2 is the smallest number")
elif number3 < number1 and number3 < number2:
    print("Number 3 is the smallest number")
else:
    print("All numbers are the same")