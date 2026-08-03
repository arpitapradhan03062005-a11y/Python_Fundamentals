string = "HELLO"

unique = ""

#create unique string
for char in string:
    if char  not in unique:
        unique = unique + char

#counts frequency of each char
for char in unique:
    count = 0
    for i in string:
        if char == i:
            count += 1
    print(char, ":", count)

