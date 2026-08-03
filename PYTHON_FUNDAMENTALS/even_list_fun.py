def even(numbers):
    e = []
    for number in numbers:
        if number % 2 == 0:
            e.append(number)
    return e

numbers = list(map(int,input("Enter numbers:").split()))
print(numbers)
print(even(numbers))