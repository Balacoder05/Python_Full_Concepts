import random

number = random.randint(1, 100)
guess = 0

while guess != number:
    guess = int(input("Guess a number (1–100): "))
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")

print("🎉 Correct! You guessed the number.")
