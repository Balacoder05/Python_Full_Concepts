marks = list(map(int, input("Enter marks: ").split()))

avg = sum(marks) / len(marks)

if avg >= 90:
    print("Grade: A")
elif avg >= 75:
    print("Grade: B")
elif avg >= 50:
    print("Grade: C")
else:
    print("Fail")
