import random

secret_number = random.randint(1, 100)

print("Guess the number!")
print("I have chosen a number between 1 and 100.")

guess = int(input("Enter your guess: "))
attempts = 1

while guess != secret_number and attempts < 5:
    if guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")

    guess = int(input("Try again: "))
    attempts += 1
if guess == secret_number:
    print("Correct! You guessed the number in", attempts, "attempts!")
else:
    print("Game over!")
    print("The number was " + str(secret_number) + ".")
