import math
number = 407
original = number 
count = 0

while number > 0:
    digit = number % 10
    number = number  // 10
    count += 1
sum = 0
temp= original
while original > 0:
    digit = original % 10 
    exp = math.pow(digit,count)
    sum = sum + exp
    original = original // 10

if temp == sum:
    print("Armstrong number")
else:
    print("NOT Armstrong number")