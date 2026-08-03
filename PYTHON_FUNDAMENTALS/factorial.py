def fact(n):
    factorial = 1
    for i in range(1,n+1):
        factorial = factorial * i
    return factorial

n = int(input("Enter no.:"))
ans = fact(n)
print(f"Factorial of {n} is {ans}")