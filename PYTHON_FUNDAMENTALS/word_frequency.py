text = "python is easy and python is powerful"

list = list(text.split(" "))
print(list)

#remove duplicates
unique = []
for word in list:
    if word not in unique:
        unique.append(word)
print(unique)
#finding frequency

for i in unique:
    count = 0
    for word in list:
        if i == word:
            count += 1
    print(i, ":", count)
