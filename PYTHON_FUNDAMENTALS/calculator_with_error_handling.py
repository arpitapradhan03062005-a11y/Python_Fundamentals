try :
    a = int(input("Enter first no.:"))
    o = input("Enter operator :")
    b = int(input("Enter second numnber:"))

    if o == "+":
        result = a + b
    elif o == "-":
        result = a - b
    elif o == "*":
        result = a * b
    elif o == "/":
        result = a / b

    print("Result :",result)

except ValueError :
    print("Invalid number!")

except ZeroDivisionError:
    print("Cannot divide by zero!")

