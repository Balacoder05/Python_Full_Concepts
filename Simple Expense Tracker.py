expenses = []

while True:
    item = input("Enter expense item (or 'stop'): ")
    if item == "stop":
        break

    amount = float(input("Enter amount: "))
    expenses.append((item, amount))

print("\n--- Expense Summary ---")
total = 0
for item, amount in expenses:
    print(item, ":", amount)
    total += amount

print("Total Expense =", total)
