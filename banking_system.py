

import random
from datetime import datetime

# Store all accounts
accounts = {}


# ---------------- CREATE ACCOUNT ----------------

def create_account():
    print("\n===== CREATE ACCOUNT =====")

    name = input("Enter your name: ")
    phone = input("Enter your phone number: ")

    pin = input("Create a 4-digit PIN: ")

    if len(pin) != 4 or not pin.isdigit():
        print("Invalid PIN! PIN must contain 4 digits.")
        return

    # Generate unique account number
    account_number = random.randint(100000, 999999)

    while account_number in accounts:
        account_number = random.randint(100000, 999999)

    # Store account details
    accounts[account_number] = {
        "name": name,
        "phone": phone,
        "pin": pin,
        "balance": 0.0,
        "transactions": []
    }

    print("\nAccount created successfully!")
    print("Your Account Number:", account_number)
    print("Please remember your account number.")


# ---------------- LOGIN ----------------

def login():
    print("\n===== LOGIN =====")

    if not accounts:
        print("No accounts available. Please create an account first.")
        return

    try:
        account_number = int(input("Enter account number: "))
    except ValueError:
        print("Invalid account number!")
        return

    pin = input("Enter PIN: ")

    if account_number in accounts:
        account = accounts[account_number]

        if account["pin"] == pin:
            print("\nLogin successful!")
            print("Welcome,", account["name"])

            account_menu(account_number)
        else:
            print("Incorrect PIN!")
    else:
        print("Account not found!")


# ---------------- ACCOUNT MENU ----------------

def account_menu(account_number):

    while True:

        print("\n===== ACCOUNT MENU =====")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. Transaction History")
        print("6. Change PIN")
        print("7. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            check_balance(account_number)

        elif choice == "2":
            deposit(account_number)

        elif choice == "3":
            withdraw(account_number)

        elif choice == "4":
            transfer(account_number)

        elif choice == "5":
            transaction_history(account_number)

        elif choice == "6":
            change_pin(account_number)

        elif choice == "7":
            print("Logged out successfully!")
            break

        else:
            print("Invalid choice! Please try again.")


# ---------------- CHECK BALANCE ----------------

def check_balance(account_number):

    account = accounts[account_number]

    print("\n===== ACCOUNT BALANCE =====")
    print("Account Holder:", account["name"])
    print("Current Balance: ₹", format(account["balance"], ".2f"))


# ---------------- DEPOSIT ----------------

def deposit(account_number):

    account = accounts[account_number]

    print("\n===== DEPOSIT MONEY =====")

    try:
        amount = float(input("Enter deposit amount: ₹"))
    except ValueError:
        print("Please enter a valid amount!")
        return

    if amount <= 0:
        print("Amount must be greater than zero.")
        return

    account["balance"] += amount

    account["transactions"].append({
        "type": "Deposit",
        "amount": amount,
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

    print("Deposit successful!")
    print("Updated Balance: ₹", format(account["balance"], ".2f"))


# ---------------- WITHDRAW ----------------

def withdraw(account_number):

    account = accounts[account_number]

    print("\n===== WITHDRAW MONEY =====")

    try:
        amount = float(input("Enter withdrawal amount: ₹"))
    except ValueError:
        print("Please enter a valid amount!")
        return

    if amount <= 0:
        print("Amount must be greater than zero.")
        return

    if amount > account["balance"]:
        print("Insufficient balance!")
        return

    account["balance"] -= amount

    account["transactions"].append({
        "type": "Withdrawal",
        "amount": amount,
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

    print("Withdrawal successful!")
    print("Remaining Balance: ₹", format(account["balance"], ".2f"))


# ---------------- TRANSFER ----------------

def transfer(account_number):

    sender = accounts[account_number]

    print("\n===== TRANSFER MONEY =====")

    try:
        receiver_number = int(input("Enter receiver account number: "))
    except ValueError:
        print("Invalid account number!")
        return

    if receiver_number not in accounts:
        print("Receiver account not found!")
        return

    if receiver_number == account_number:
        print("You cannot transfer money to your own account!")
        return

    try:
        amount = float(input("Enter transfer amount: ₹"))
    except ValueError:
        print("Please enter a valid amount!")
        return

    if amount <= 0:
        print("Amount must be greater than zero.")
        return

    if amount > sender["balance"]:
        print("Insufficient balance!")
        return

    receiver = accounts[receiver_number]

    sender["balance"] -= amount
    receiver["balance"] += amount

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    sender["transactions"].append({
        "type": "Transfer Sent",
        "amount": amount,
        "to": receiver_number,
        "time": current_time
    })

    receiver["transactions"].append({
        "type": "Transfer Received",
        "amount": amount,
        "from": account_number,
        "time": current_time
    })

    print("Transfer successful!")
    print("Transferred ₹", format(amount, ".2f"))
    print("Remaining Balance: ₹", format(sender["balance"], ".2f"))


# ---------------- TRANSACTION HISTORY ----------------

def transaction_history(account_number):

    account = accounts[account_number]

    print("\n===== TRANSACTION HISTORY =====")

    transactions = account["transactions"]

    if not transactions:
        print("No transactions yet.")
        return

    for index, transaction in enumerate(transactions, start=1):

        print("\nTransaction", index)
        print("Type:", transaction["type"])
        print("Amount: ₹", format(transaction["amount"], ".2f"))
        print("Time:", transaction["time"])

        if "to" in transaction:
            print("Receiver Account:", transaction["to"])

        if "from" in transaction:
            print("Sender Account:", transaction["from"])


# ---------------- CHANGE PIN ----------------

def change_pin(account_number):

    account = accounts[account_number]

    print("\n===== CHANGE PIN =====")

    old_pin = input("Enter old PIN: ")

    if old_pin != account["pin"]:
        print("Incorrect old PIN!")
        return

    new_pin = input("Enter new 4-digit PIN: ")
    confirm_pin = input("Confirm new PIN: ")

    if len(new_pin) != 4 or not new_pin.isdigit():
        print("Invalid PIN! PIN must contain 4 digits.")
        return

    if new_pin != confirm_pin:
        print("PINs do not match!")
        return

    if new_pin == old_pin:
        print("New PIN must be different from old PIN!")
        return

    account["pin"] = new_pin

    print("PIN changed successfully!")


# ---------------- MAIN MENU ----------------

def main():

    while True:

        print("\n==============================")
        print("       BANKING SYSTEM")
        print("==============================")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_account()

        elif choice == "2":
            login()

        elif choice == "3":
            print("Thank you for using Banking System!")
            break

        else:
            print("Invalid choice! Please try again.")


# Start the program
main()
