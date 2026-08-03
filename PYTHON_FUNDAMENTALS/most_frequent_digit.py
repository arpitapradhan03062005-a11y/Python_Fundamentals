numbers = [1, 2, 2, 3, 3, 3, 4, 2, 5]

unique = []

for num in numbers:
    if num not in unique:
        unique.append(num)

print(unique)

freq = {}

for i in unique:
    count = 0
    for num in numbers:
        if i == num:
            count += 1
        freq.update({i : count})

print(freq)

highest = 0
element = None

for key, value in freq.items():

    if value > highest:
        highest = value
        element = key

print("Most frequent:", element)
print("Frequency:", highest)