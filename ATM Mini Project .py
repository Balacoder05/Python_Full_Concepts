balance = 5000

while True:
    print("\n1.Deposit\n2.Withdraw\n3.Balance\n4.Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        amt = int(input("Enter deposit amount: "))
        balance += amt
        print("Deposited ✅")

    elif choice == 2:
        amt = int(input("Enter withdraw amount: "))
        if amt <= balance:
            balance -= amt
            print("Withdrawn ✅")
        else:
            print("Insufficient Balance ❌")

    elif choice == 3:
        print("Current Balance =", balance)

    elif choice == 4:
        print("Thank you 👋")
        break
