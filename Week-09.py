import pickle

class Customer:
    def __init__(self):
        self.cid = ''
        self.cname = ''
        self.acc_no = ''
        self.balance = ''
        self.credit_card = []

    def create_customer(self):
        cid = str(input("Enter Customer ID: "))
        cname = str(input("Enter Customer Name: "))
        acc_no = int(input("Enter Customer Account Number: "))
        balance = int(input("Enter Customer Balance: "))
        credit_card = Customer()
        credit_card.cid = cid
    def display_customer(self):
        print('cid:', self.cid )
        print('cname:', self.cname )
        print('acc_no:', self.acc_no)
        print('balance:', self.balance)
        print('credit_card:', self.credit_card)
    def transfer_funds(bene_cust_obj, amount):
        self.balance = amount
        bene_cust_obj.balance += amount
    def assign_card(selfcard_obj ):
        self.credit_card.append(card.obj)

class Card:
    def __init__(self):
        self.card_no = ''
        self.expiry_date = ''
        self.cvv = ''
        self.balance = ''
    def add_card(self):
        self.card_no = int(input("Enter Card No: "))
        self.expiry_date = int(input("Enter Expiry Date: "))
        self.cvv = int(input("Enter CVV: "))
        self.balance = int(input("Enter Balance: "))
    def display_card(self):
        print('card_no:', self.card_no)
        print('expiry_date:', self.expiry_date)
        print('cvv:', self.cvv)
        print('balance:', self.balance)

CustomerList = []
CardList = []
while True:
    print("1: Create Customer : ")
    print("2: Create Card : ")
    print("3: Transfer funds between customer : ")
    print("4: Assign card to customer :")
    print("5: Display customer information : ")
    print("6: Display Card information : ")
    print("7: Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        create_customer = Customer()
        create_customer.create_customer()
    elif choice == 2:
        create_card_obj = Card()
        create_card_obj.add_card()
    elif choice == 3:
        print_card_obj = Card()
    elif choice == 4:
        display_customer = Customer()
        display_customer.display_customer()

    elif choice == 5:
        display_customer = Customer()
        display_customer.display_customer()
    elif choice == 6:
        display_card_obj = Card()
        display_card_obj.display_card()
    elif choice == 7:
        break
