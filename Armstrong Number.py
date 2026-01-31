n = int(input("Enter number: "))
temp = n
sum = 0

while temp > 0:
    d = temp % 10
    sum += d ** 3
    temp //= 10

if sum == n:
    print("Armstrong number")
else:
    print("Not Armstrong")
