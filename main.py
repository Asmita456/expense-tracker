import json
from datetime import datetime
from pathlib import Path

DATA_FILE = Path(__file__).parent / "expenses.json"

def load_expenses():
    if not DATA_FILE.exists():
        return []

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)

    except json.JSONDecodeError:
        return []

def save_expenses(expenses):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(expenses, file, indent = 4)


def add_expense(expenses):
    title = input("Enter expense title: ")
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))
    date = input("Enter date (YYYY-MM-DD): ")
    note = input("Enter note (optional): ")

    expense = {
        "title": title,
        "category": category,
        "amount" : amount,
        "date" : date,
        "note" : note
    }

    expenses.append(expense)
    save_expenses(expenses)

def view_expenses(expenses):

    if not expenses:
        print("No expenses found.")
        return

    print("\n------- All Expenses -------")

    for index, expense in enumerate(expenses, start = 1):
        print(f"\n Expense {index}")
        print(f"Title: {expense['title']}")
        print(f"Category: {expense['category']}")
        print(f"Amount: Rs. {expense['amount']:.2f}")
        print(f"Date: {expense['date']}")
        print(f"Note: {expense['note']}")

def show_summary(expenses):
    if not expenses:
        print("No expenses found.")
        return

    total = sum(expense["amount"] for expense in expenses)
    average = total / len(expenses)

    print("\n--- Expense Summary ---")
    print(f"Total Expenses: Rs. {total:.2f}")
    print(f"Number of Expenses: {len(expenses)}")
    print(f"Average Expense: Rs. {average:.2f}")

    category_totals = {}

    for expense in expenses:
        category = expense["category"]

        if category in category_totals:
            category_totals[category] += expense["amount"]
        else:
            category_totals[category] = expense["amount"]

    print("\n--- Category-wise Summary ---")

    for category, amount in category_totals.items():
        print(f"{category}: Rs. {amount:.2f}")

def filter_by_category(expenses):
    category = input("Enter category to filter: ").strip()

    found = False

    for expense in expenses:
        if expense["category"].lower() == category.lower():
            print(f"\nTitle: {expense['title']}")
            print(f"Category: {expense['category']}")
            print(f"Amount: Rs. {expense['amount']:.2f}")
            print(f"Date: {expense['date']}")
            print(f"Note: {expense['note']}")
            found = True

    if not found:
        print("No expenses found in this category.")

def delete_expense(expenses):
    if not expenses:
        print("No expenses to delete.")
        return

    view_expenses(expenses)

    try:
        number = int(input("\nEnter expense number to delete: "))

        if 1 <= number <= len(expenses):
            removed = expenses.pop(number - 1)
            save_expenses(expenses)

            print(f"Expense '{removed['title']}' deleted successfully!")
        else:
            print("Invalid expense number.")

    except ValueError:
        print("Please enter a valid number.")

def main():
    expenses = load_expenses()

    while True:
        print("\n===== EXPENSE TRACKER =====")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Show Expense Summary")
        print("4. Filter by Category")
        print("5. Delete Expense")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            show_summary(expenses)
        elif choice == "4":
            filter_by_category(expenses)
        elif choice == "5":
            delete_expense(expenses)
        elif choice == "6":
            print("Thank you for using Expense Tracker!")
            break
        else:
            print("Invalid choice. Please select 1-6.")


if __name__ == "__main__":
    main()