total = 0

while True:
    amount = input("Enter expense amount (or 'q' to quit): ")
    if amount == 'q':
        break
    total += float(amount)

print("Total Expense:", total)