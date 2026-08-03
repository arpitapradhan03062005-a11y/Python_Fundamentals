list = [1,67,77,99,99,12,45]

new_list = []

#removes duplicate
for item in list:
    if item not in new_list:
        new_list.append(item)

#finding the second largest
largest = list[0]
second_largest = list[0]

for item in new_list:
    if item > largest:
        second_largest = largest
        largest = item

    elif item > second_largest and item != largest:
        second_largest = item

print(second_largest)
