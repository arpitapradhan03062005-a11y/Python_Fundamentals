text = "Python@123AI!"

upper_count = 0
lower_count = 0
digit_count = 0
char_count = 0

for char in text:
    if char.isupper() == True:
        upper_count += 1

    elif char.islower() == True:
        lower_count += 1

    elif char.isdigit() == True:
        digit_count += 1

    else:
        char_count += 1

print("Upper :",upper_count)
print("Lower :",lower_count)
print("Digit :",digit_count)
print("Character :",char_count)