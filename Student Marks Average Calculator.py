marks = []

n = int(input("How many subjects? "))

for i in range(n):
    m = int(input(f"Enter mark {i+1}: "))
    marks.append(m)

avg = sum(marks) / n

print("Average =", avg)
