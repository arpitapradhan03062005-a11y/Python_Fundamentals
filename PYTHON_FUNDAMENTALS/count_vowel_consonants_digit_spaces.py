import string
text = "Python is 123 easy"

list = text.split()

vowels = "aeiou"
vowels_count = 0

consonants = "bcdfghjklmnpqrstvwxyz"
consonants_count = 0

digits = string.digits
digits_count = 0

space_count = 0

for char in text.lower():
    if char in vowels:
        vowels_count += 1

    if char in consonants:
        consonants_count += 1

    if char in digits:
        digits_count += 1

    if char == " ":
        space_count += 1
    
print("Vowels :",vowels_count)
print("Consonants :",consonants_count)
print("Digits :",digits_count)
print("Spaces :",space_count)