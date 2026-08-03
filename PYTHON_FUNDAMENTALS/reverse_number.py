number = 1234
reversed : int = 0

while number > 0:
    digit = number % 10
    reversed = reversed * 10 + digit
    number = number // 10 


print(reversed)