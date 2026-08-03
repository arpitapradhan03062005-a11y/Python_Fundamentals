#5! = 5 × 4 × 3 × 2 × 1 = 120

def factorial(n):
    if n < 0:
        return "Invalid number"
    else:
        if n == 0:
            return 1
        else:
            return n * factorial(n-1)

n = int(input("Enter number :"))
print(factorial(n))