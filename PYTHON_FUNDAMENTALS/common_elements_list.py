list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8, 9]

common = []
for item1 in list1:
    for item2 in list2:
        if item1 == item2 and item1 not in common:
            common.append(item1)

print(common)