
def vowel(str):
    count = 0
    new_str = str.lower()
    for char in new_str:
        if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
            count += 1 
    return count

str = input("Enter string:")
print(vowel(str))