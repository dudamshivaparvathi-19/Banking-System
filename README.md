
#  Python Banking System

# Project Description

The Python Banking System is a console-based banking application developed using Python.

This project allows users to create a bank account, log in using their account number and PIN, check their balance, deposit money, withdraw money, transfer money to another account, view transaction history, and change their PIN.

The project is developed to understand Python programming concepts such as functions, dictionaries, conditional statements, loops, exception handling, and data structures.

---

# Features

- ✅ Create a new bank account
- ✅ Generate a unique account number
- ✅ Login using account number and PIN
- ✅ Check account balance
- ✅ Deposit money
- ✅ Withdraw money
- ✅ Transfer money between accounts
- ✅ View transaction history
- ✅ Change account PIN
- ✅ Validate user input
- ✅ Logout from the account
- ✅ Exit the banking system

---

# Technologies Used

- **Programming Language:** Python
- **Modules Used:**
  - `random`
  - `datetime`
- **Data Storage:** Python Dictionary
- **Interface:** Command Line Interface (CLI)
- **Development Environment:** Visual Studio Code

---

# Project Structure

```text
Banking-System/
│
├── banking_system.py
│
└── README.md
```

---

# Requirements

Before running the project, make sure you have:

1. Python 3 installed
2. Visual Studio Code (recommended)
3. Python extension in VS Code (optional but recommended)

---

# How to Run the Project

## Step 1: Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

## Step 2: Open the Project Folder

```bash
cd Banking-System
```

### Step 3: Run the Python Program

```bash
python banking_system.py
```

If the `python` command does not work on Windows, try:

```bash
py banking_system.py
```

---

# Main Menu

When the program runs, the following menu is displayed:

```text
==============================
       BANKING SYSTEM
==============================
1. Create Account
2. Login
3. Exit
Enter your choice:
```

---

# Working of the Project

## 1. Create Account

- The user enters their name and phone number.
- The user creates a 4-digit PIN.
- The system generates a unique account number.
- Account details are stored in a Python dictionary.
- The initial balance is set to ₹0.00.

## 2. Login

- The user enters their account number and PIN.
- The system verifies the login details.
- After successful login, the user can access the account menu.

## 3. Deposit

- The user enters the amount to deposit.
- The amount is added to the account balance.
- The transaction is recorded in the transaction history.

## 4. Withdraw

- The user enters the withdrawal amount.
- The system checks whether sufficient balance is available.
- If the balance is sufficient, the amount is deducted.

## 5. Transfer

- The user enters the receiver's account number.
- The system verifies the receiver's account.
- The transfer amount is deducted from the sender.
- The amount is added to the receiver.
- Both accounts receive a transaction record.

## 6. Transaction History

- The system displays previous transactions.
- It shows the transaction type, amount, and time.
- Transfer records include sender or receiver account details.

# 7. Change PIN

- The user enters the old PIN.
- The system verifies the old PIN.
- The user enters and confirms a new 4-digit PIN.
- The PIN is updated if the validation checks pass.

---

# Python Concepts Used

| Concept | Usage |
|---|---|
| Functions | Separate functions for each banking operation |
| Dictionary | Store account details |
| Nested Dictionary | Store individual account information |
| Lists | Store transaction history |
| While Loop | Display menus repeatedly |
| If-Else | Validate conditions and choices |
| Try-Except | Handle invalid numeric input |
| Random Module | Generate account numbers |
| Datetime Module | Record transaction timestamps |
| String Methods | Validate the 4-digit PIN |

---

# 📸 Sample Output

```text
===== CREATE ACCOUNT =====
Enter your name: Shiva
Enter your phone number: 9876543210
Create a 4-digit PIN: 1234

Account created successfully!
Your Account Number: 456789
Please remember your account number.
```

---

# Data Storage and Limitations

This project is developed for educational purposes.

- Account information is stored temporarily in Python memory.
- Data is lost when the program is closed.
- The project does not use a database.
- The PIN is stored as plain text in memory.
- This project is not intended for real banking or financial transactions.

---

# Future Enhancements

- Add database connectivity using SQLite or MySQL.
- Implement secure PIN hashing.
- Add an admin login system.
- Add account deletion functionality.
- Generate bank statements.
- Add a graphical user interface (GUI).
- Add persistent data storage.
- Improve authentication and input validation.

---

# Author

**Shiva Parvathi**

Python Programming Project

---

#  License

This project is created for educational and learning purposes.
