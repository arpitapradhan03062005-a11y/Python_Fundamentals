numbers = [5, 2, 8, 1, 9, 3]

smallest = numbers[0]

sort = []

for num in numbers:
    if num < smallest:
        smallest = num
        sort.append(smallest)

print(sort)