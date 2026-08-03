import random

number = random.randint(1,50)
attempts = 0

while attempts < 5:
    n = int(input(("Guess the number:")))
    attempts += 1
    if n == number:
        print("Correct!")
        break
    elif n < number:
        print("Too low")
    else:
        print("Too high")

if n == number:
    print(f"You guessed it in {attempts} attempts.")
else:
    print("Game Over!")
    print("The number was:", number)
   
