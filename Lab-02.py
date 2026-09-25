employees = {}

def add_employee(n):
    employeeName = input("Enter employee name: ")
    BasicPay = int(input("Enter Basic Pay: "))
    allowance = int(input("Enter your allowance: "))
    deduction = int(input("Enter your deduction: "))
    taxes = int(input("Enter your taxes: "))
    gross_pay = BasicPay + allowance
    net_pay = gross_pay - deduction - taxes
    employees.update(
    {"e"+str(n):
        {
            "name":employeeName,
            "basicPay":BasicPay,
            "allowance":allowance,
            "deduction":deduction,
            "taxes":taxes
        }
    })
def del_employee():
    delt_name = input("Enter employee name: ")
    del employees[delt_name]

def modify_employee():
    edit_name = input("Enter employee name you want to modify: ")
    new_emp_name = input("Enter new employee name: ")
    new_basic_pay = int(input("Enter new Basic Pay: "))
    new_allowance = int(input("Enter new allowance: "))
    new_deduction = int(input("Enter new deduction: "))
    new_taxes = int(input("Enter new taxes: "))
    new_gross_pay = new_basic_pay + new_allowance
    new_net_pay = new_basic_pay - new_allowance - new_deduction
    employees.update(
        {"name" + str(i):
            {
                "name": new_emp_name,
                "basicPay": new_basic_pay,
                "allowance": new_allowance,
                "deduction": new_deduction,
                "taxes": new_taxes
            }
        }
        )
def display():
    print(employees)

i = 1
while True:
    print("1: Add an employee ")
    print("2: Delete an employee ")
    print("3: Modify an employee ")
    print("4: Display all employee ")
    print("5: Exit")
    choice = int(input("Enter your choice: "))


    if(choice == 1):
        add_employee(i)
        i = i+1
    elif(choice == 2):
        del_employee()
    elif choice == 3:
        modify_employee()
    elif(choice == 4):
        display()
    elif(choice == 5):
        break



