list = ["arpita", "arpita", "ram","ram" ,"krishna"]

for item in list:
    if list.count(item) >= 2:
        list.remove(item)
print(list)