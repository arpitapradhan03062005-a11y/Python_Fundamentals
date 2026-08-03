text = "programming"

unique = ""
#create unique string
for char in text:
    if char  not in unique:
        unique = unique + char

dict = {}
#counts frequency of each char
for char in unique:
    count = 0
    for i in text:
        if char == i:
            count += 1
    dict.update({char:count})

highest = max(dict.values())

for char, count in dict.items():
    if count == highest:
        print(char ,":",count)


