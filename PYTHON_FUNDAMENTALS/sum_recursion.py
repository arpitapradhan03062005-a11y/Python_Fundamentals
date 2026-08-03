def sum_numbers(n):
    if n == 0 :
        return 0
    else:
        digit = n % 10
        return  digit + sum_numbers(n//10)

n = int(input("Enter number :"))
print(sum_numbers(n))