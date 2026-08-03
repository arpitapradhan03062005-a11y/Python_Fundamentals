# number = 123456

# count = 0

# str = str(number)

# for i in str:
#     count += 1

# print(count)

number = 12345656767
count = 0

while number > 0:
    digit = number % 10
    number = number  // 10
    count += 1

print(count)