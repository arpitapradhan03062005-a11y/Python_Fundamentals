def menu(c,a,b):
    if c == 1:
        return a+b
    elif c == 2:
        return a-b
    elif c == 3:
        return a*b
    elif c == 4:
        return a/b
    else:
        return "Invalid choice"
while True:
    print("MENU :\n")
    print("1.ADDITION")
    print("2.SUBSTRACTION")
    print("3.MULTIPLICATION")
    print("4.DIVISION")
    print("5.EXIT")

    c = int(input("Enter choic:"))
    if c == 5:
        print("Exiting...")
        break
    if c > 5:
        print("Invalid choice!!")
        break

    a = int(input("Enter first number:"))
    b = int(input("Enter second number:"))

    result = menu(c, a, b)
    print("Result:", result)
