str = "mam"

reversed = ""

#generate reverse
for i in str:
    reversed = i + reversed 

if str == reversed:
    print("Palindrome")
else:
    print("Not Palindrome")