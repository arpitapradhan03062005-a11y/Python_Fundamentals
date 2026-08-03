import random

print("1. Easy (1 - 10)")
print("2. Medium (1 - 50)")
print("3. Hard (1 - 100)")

choice = int(input("Enter choice :"))

if choice == 1:
    number = random.randint(1,10)

elif choice == 2:
    number = random.randint(1,50)

elif choice == 3:
    number = random.randint(1,100)
    
attempts = 1

while True:
    n = int(input("Enter number :"))
    
    if n < number:
        print("Too low!!")
        attempts += 1
    elif n > number:
        print("Too high!")
        attempts += 1
    else:
        print("Corect!")
        print(f"Gussed in {attempts} attempts")
        break
