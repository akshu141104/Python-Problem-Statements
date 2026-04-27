
"""
Project 2 : "Personal Expense Tracker (CLI)"
Problem Statement:
You want to track your daily expenses from the terminal. You should be able to add an expense, view all expenses by category, get monthly totals, and save/load data from a text file so data persists between sessions.
Stack: Python, file I/O (no database yet)
Input: Category (food/travel/bills), amount, date (typed)
Output: Category-wise summary, total spending, daily breakdown
Think about:
How do you structure each expense record? (dict per record)
How do you read/write to a file so data isn't lost on exit?
What if the file doesn't exist on first run?
How do you handle duplicate categories with different cases (Food vs food)?

"""


import os

file_name = "expenses.txt"

while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = input("Enter choice: ")

    # ADD EXPENSE
    if choice == "1":
        category = input("Enter category: ").lower()
        amount = input("Enter amount: ")
        date = input("Enter date (DD-MM-YYYY): ")

        file = open(file_name, "a")
        file.write(category + "," + amount + "," + date + "\n")
        file.close()

        print("Expense added!")

    # VIEW EXPENSES
    elif choice == "2":
        if not os.path.exists(file_name):
            print("No data found!")
        else:
            file = open(file_name, "r")
            data = file.readlines()
            file.close()

            print("\n--- All Expenses ---")
            for line in data:
                print(line.strip())

    # EXIT
    elif choice == "3":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")