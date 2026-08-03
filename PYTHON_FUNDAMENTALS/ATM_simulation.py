balance = 10000
while True:
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Enter your choice :"))

    if choice == 1:
        print("Balance :",balance)
    elif choice == 2:
        amount = int(input("Enter amount:"))
        balance = balance + amount
        print("Amount Deposited!")
        print("Current Balance :",balance)
    elif choice == 3:
        amount = int(input("Enter amount:"))
        if amount > balance:
            print("Not enough Balance!!")
        else:
            balance = balance - amount
            print("Amount Withdrawn!")
            print("Current Balance :",balance)
    elif choice == 4:
        break
    else:
        print("Invalid choice!")

