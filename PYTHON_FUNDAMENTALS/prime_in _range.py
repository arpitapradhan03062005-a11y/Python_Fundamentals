def is_prime(n):
    if n < 2:
        return False
    for i in range(2,n):
        if n % i == 0 :
            return False
    return True

start = int(input("Enter starting range :"))
end = int(input("Enter ending range :"))

numbers = []
prime = []
for i in range(start,end+1):
    numbers.append(i)
print(numbers)

for num in numbers:
    if is_prime(num):
        prime.append(num)

print(prime)