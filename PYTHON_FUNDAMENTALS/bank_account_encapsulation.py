class BankAccount:
    def __init__(self,balance):
        self.__balance = balance

    def deposit(self,amount):
        if amount <= 0:
            print("Invalid amount")
        else:
            self.__balance += amount
            print("Balance : ",self.__balance)

    def withdraw(self,amount):
            if amount <= 0:
                print("Invalid amount")
            elif self.__balance < amount:
                print("Not enough balance")
            else:
                self.__balance -= amount
                print("Balance : ",self.__balance)

    def get_balance(self):
            print("Balance :",self.__balance)

object = BankAccount(10000)
object.get_balance()

    