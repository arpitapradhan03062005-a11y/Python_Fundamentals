str = input("Enter string:")
reversed = ""

for char in str:
    reversed = char + reversed

print(reversed)
