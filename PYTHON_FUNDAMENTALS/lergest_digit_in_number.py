number = 583921
number = abs(number)
largest = 0
while number > 0:
    digit = number % 10
    if largest < digit:
        largest = digit
    number = number // 10

print (largest)