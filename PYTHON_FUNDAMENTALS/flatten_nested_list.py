numbers = [
    [1, 2, 3],
    [4, 5],
    [6, 7, 8]
]

new_list = []
for number in numbers:
    for num in number:
        new_list.append(num)

print(new_list)