class BankAccount:
    def __init__(self,account_holder,balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self,amount):
        if amount <= 0:
            print("Invalid amount")
        else:
            self.balance += amount
            print("Balance : ",self.balance)

    def withdraw(self,amount):
        if amount <= 0:
            print("Invalid amount")
        elif self.balance < amount:
            print("Not enough balance")
        else:
            self.balance -= amount
            print("Balance : ",self.balance)

    def check_balance(self):
        print("Balance :",self.balance)

name = input("Enter account holder name :")
balance = int(input("Enter balance :"))
customer1 = BankAccount(name,balance)
customer1.check_balance()
amount = int(input("Enter amount :"))
customer1.deposit(amount)
amount = int(input("Enter amount :"))
customer1.withdraw(amount)

