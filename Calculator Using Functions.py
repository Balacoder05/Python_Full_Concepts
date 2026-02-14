def add(a, b): return a + b
def sub(a, b): return a - b

x = int(input("Enter x: "))
y = int(input("Enter y: "))

print("1.Add 2.Sub")
choice = int(input("Choice: "))

if choice == 1:
    print("Result:", add(x, y))
else:
    print("Result:", sub(x, y))
