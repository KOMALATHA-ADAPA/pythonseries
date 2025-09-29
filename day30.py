import csv
from datetime import datetime

class Expense:
    def __init__(self, amount, category, description):
        self.amount = amount
        self.category = category
        self.description = description
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

class ExpenseTracker:
    def __init__(self, filename="expenses.csv"):
        self.filename = filename
        self.expenses = []
        self.load_expenses()

    def add_expense(self, amount, category, description=""):
        try:
            amount = float(amount)
            expense = Expense(amount, category, description)
            self.expenses.append(expense)
            self.save_expenses()
            print(" Expense added successfully!")
        except ValueError:
            print(" Invalid amount. Please enter a number.")

    def view_expenses(self):
        if not self.expenses:
            print("No expenses recorded yet.")
        for e in self.expenses:
            print(f"{e.date} | {e.category} | {e.amount} | {e.description}")

    def total_by_category(self, category):
        total = sum(e.amount for e in self.expenses if e.category == category)
        print(f" Total spent on {category}: {total}")

    def save_expenses(self):
        with open(self.filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount", "Description"])
            for e in self.expenses:
                writer.writerow([e.date, e.category, e.amount, e.description])

    def load_expenses(self):
        try:
            with open(self.filename, "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    expense = Expense(float(row["Amount"]), row["Category"], row["Description"])
                    expense.date = row["Date"]
                    self.expenses.append(expense)
        except FileNotFoundError:
            pass  # No file yet

# --- Running the Expense Tracker ---
tracker = ExpenseTracker()

while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Total by Category")
    print("4. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        amt = input("Enter amount: ")
        cat = input("Enter category: ")
        desc = input("Enter description (optional): ")
        tracker.add_expense(amt, cat, desc)

    elif choice == "2":
        tracker.view_expenses()

    elif choice == "3":
        cat = input("Enter category: ")
        tracker.total_by_category(cat)

    elif choice == "4":
        print("Exiting... Goodbye ")
        break
    else:
        print(" Invalid choice, try again.")
