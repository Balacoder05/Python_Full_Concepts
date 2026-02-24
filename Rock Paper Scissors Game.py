import random

choices = ["rock", "paper", "scissors"]
computer = random.choice(choices)
user = input("Enter rock/paper/scissors: ")

print("Computer:", computer)

if user == computer:
    print("Draw")
elif (user == "rock" and computer == "scissors") or \
     (user == "paper" and computer == "rock") or \
     (user == "scissors" and computer == "paper"):
    print("You Win 🎉")
else:
    print("You Lose ❌")