number = 123443
original = number 

reversed = 0
#reverse number
while number > 0:
    digit = number % 10
    reversed = reversed * 10 + digit
    number = number // 10

if original == reversed :
    print("Palindrome")
else:
    print("Not Palindrome")