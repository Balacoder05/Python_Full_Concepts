import random

names = ["Ravi", "Bala", "Kumar", "Arun"]
places = ["Chennai", "Delhi", "Mumbai", "Bangalore"]
actions = ["found a treasure", "met an alien", "won a lottery", "became a hero"]

name = random.choice(names)
place = random.choice(places)
action = random.choice(actions)

print(name, "went to", place, "and", action)