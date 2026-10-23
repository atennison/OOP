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
    def transfer_funds(self, bene_cust_obj, amount):
       self.balance = self.balance - amount
        bene_cust_obj.balance = bene_cust_obj.balance + amount
        print("Transfer successful!)

    def assign_card(selfcard_obj ):
        self.credit_card.append(card.obj)
        print("Card assigned successfully!")
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
        customer = Customer()
        customer.create_customer()
        CustomerList.append(customer)
        
    elif choice == 2:
        card= Card()
        card.add_card()
        CardList.append(card)
    elif choice == 3:
        for customer in CustomerList
            print(customer.cname)
        sender = int(input("Enter sender customer number: "))
        receiver = int(input("Enter receiver customer number: "))
        amount = float(input("Enter amount to transfer: "))
         CustomerList[sender - 1].transfer_funds(
            CustomerList[receiver - 1], amount
        )

    elif choice == 4:
        for customer in CustomerList
            print(customer.cname)
        customer_num = int(input("Enter card number: ")
        for card in CardList:
            print(card..card_no)
        card_num = int(input("Enter card number: ")
        CustomerList[customer_num - 1].credit_card.appened(
            CardList[card_num - 1])
        print("Card assigned successfully)
    elif choice == 5:
        display_customer = Customer()
        display_customer.display_customer()
    elif choice == 6:
        display_card_obj = Card()
        display_card_obj.display_card()
    elif choice == 7:
        break
