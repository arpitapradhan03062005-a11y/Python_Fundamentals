import random
import string

l = int(input("Enter string length :"))

scope = string.ascii_letters + string.digits

password = ""
for i in range(l):
    password += random.choice(scope)

print("PASSWORD :",password)