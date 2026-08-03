try:
    n = int(input("Enter number:"))
except ValueError:
    print("Invalid input! Please enter a number.")
else:
    print("You entered :",n)