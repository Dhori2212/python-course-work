bal = 100000
trans = []

def withdraw(amount):
    global bal
    if amount > bal:
        print("Insufficient balance")
    else:
        bal -= amount
        trans.append(-amount)
        print("Withdrawn:", amount)

def deposit(amount):
    global bal
    bal += amount
    trans.append(amount)
    print("Deposited:", amount)

def check_balance():
    print("Current balance:", bal)

def transaction_history():
    print("Transaction history:")
    if not trans:
        print("No transactions yet.")
    else:
        for i, t in enumerate(trans, start=1):
            if t > 0:
                print(f"{i}. Deposited: {t}")
            else:
                print(f"{i}. Withdrawn: {-t}")

while True:
    print("\n1. Withdraw")
    print("2. Deposit")
    print("3. Check Balance")
    print("4. View Transaction History")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        amt = float(input("Enter amount to withdraw: "))
        withdraw(amt)
    elif choice == '2':
        amt = float(input("Enter amount to deposit: "))
        deposit(amt)
    elif choice == '3':
        check_balance()
    elif choice == '4':
        transaction_history()
    elif choice == '5':
        print("Thank you for using our service!")
        break
    else:
        print("Invalid choice. Please try again.")

