numbers = [1,2,3,4,5,2,2,3,1,4]
new_list = []
#removes duplicates
for num in numbers:
    if num not in new_list:
        new_list.append(num)
print(new_list)

#cheks frequency for each character 
for num in new_list:
    count = 0
    for i in numbers:
        if i == num:
            count += 1
    print(f"Number: {num} \t Frequency: {count}")
