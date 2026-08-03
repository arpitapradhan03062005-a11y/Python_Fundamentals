text = "aabbcdde"
unique = {}
for char in text:
    if char in unique:
        unique[char] += 1
    else:
        unique[char] = 1

print(unique)

for key,value in unique.items():
    if value == 1:
        print("First non-repeating character is :",key)
        break