number1 = int(input("Enter a number1: "))
number2 = int(input("Enter a number2: "))
operator = input("Enter a operator: ")
print("if division demonamtor should be less than 0")

if operator == "+":
    c=number1+number2
    print(c)
elif operator == "-":
    d=number1-number2
    print(d)
elif operator == "*":
    e=number1*number2
    print(e)
elif operator == "/":
    print("if division demonamtor should be less than 0")
    f=number1/number2
    print(f)
else:
    print("Invalid operator")