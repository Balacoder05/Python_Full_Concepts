import time

sentence = "Python is powerful and easy to learn"
print("Type the following sentence:\n")
print(sentence)

start = time.time()
typed = input("\nStart typing: ")
end = time.time()

time_taken = end - start

if typed == sentence:
    print("Correct!")
else:
    print("There were mistakes.")

print("Time taken:", round(time_taken, 2), "seconds")