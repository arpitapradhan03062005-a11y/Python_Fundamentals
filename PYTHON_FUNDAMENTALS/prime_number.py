# def prime(n):

#     if n < 2:
#             print("NOT Prime")
#     elif n == 2:
#             print("Prime")

#         for i in range(2,n):
#             if n % i == 0:
#                 print("NOT Prime")

#                 break
#     else:
#                 print("Prime")
#                 break

# n = int(input("Enter number:"))
# prime(n)

def prime(n):
    if n < 2:
        print("Not Prime")
        return

    for i in range(2,n):
        if n % i == 0:
            print("Not Prime")
            return

    print("Prime")
    
n = int(input("Enter no.:"))
prime(n)