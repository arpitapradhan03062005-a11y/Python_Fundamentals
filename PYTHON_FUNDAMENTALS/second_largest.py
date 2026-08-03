list = [1,2,33,33,4,2,6,8,90,90]

for item in list:
    if list.count(item) >= 2:
        list.remove(item)

list.sort()
print("Second largest :", list[-2])