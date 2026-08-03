text = "python is easy and python is powerful and python is useful"

unique = {}
duplicates = []

str = text.split(" ")

for word in str:
    if word in unique:
        unique[word] += 1
    else:
        unique[word] = 1

for key,value in unique.items():
    if value >= 2:
        duplicates.append(key)


print(duplicates)