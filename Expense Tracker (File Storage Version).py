import csv

def add_expense():
    name = input("Enter expense name: ")
    amount = float(input("Enter amount: "))

    with open("expenses.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, amount])

    print("Expense Added!")

def view_expense():
    total = 0
    with open("expenses.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(f"{row[0]} - ₹{row[1]}")
            total += float(row[1])
    print("Total Expense: ₹", total)

while True:
    print("\n1. Add Expense\n2. View Expense\n3. Exit")
    choice = input("Choose: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expense()
    elif choice == "3":
        break