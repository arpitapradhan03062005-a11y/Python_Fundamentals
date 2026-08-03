numbers = [1, 2, 3, 2, 4, 5, 3, 6, 2, 7]

unique = []

for number in numbers:
    if number not in unique:
        unique.append(number)

print(unique)


duplicates = []
for i in unique:
    count = 0
    for num in numbers:
        if i == num:
            count += 1
    if count > 1:
        duplicates.append(i)

print(duplicates)
