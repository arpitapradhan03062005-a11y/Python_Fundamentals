import random

number = random.randint(1,50)
count = 1

while True:
    n = int(input(("Guess the number:")))
    if n == number:
        print("Correct!")
        break
    elif n < number:
        print("Too low")
    else:
        print("Too high")
    count += 1


print(f"Guessed in {count} counts")