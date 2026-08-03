def greatest(a,b,c):
    if a > b and a > c:
        print("Greatest : ",a)
    elif b > a and b > c :
        print("Greatest : ",b)
    else:
        print("Greatest :", c)

a = int(input("Enter first no.:"))
b = int(input("Enter second no.:"))
c = int(input("Enter third no.:")) 

greatest(a,b,c)