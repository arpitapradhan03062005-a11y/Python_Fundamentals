numbers = [12, 7, 5, 18, 21, 30, 44, 9]

even = []
odd = []

for number in numbers:
    if number % 2 == 0:
        even.append(number)

    else:
        odd.append(number)

print("EVEN :",even)
print("ODD :",odd)