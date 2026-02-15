dict1 = {"python": "Programming Language", "cpu": "Central Processing Unit"}

word = input("Enter word: ")

print("Meaning:", dict1.get(word, "Not Found"))
