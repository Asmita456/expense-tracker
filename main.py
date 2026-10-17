
import json
import math
from datetime import datetime
from pathlib import Path

DATA_FILE = Path(__file__).parent / "expenses.json"


# Load expenses from JSON file
def load_expenses():
    if not DATA_FILE.exists():
        return []

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            expenses = json.load(file)

        if isinstance(expenses, list):
            return expenses

        print("Warning: Invalid expense data format.")
        return []

    except (json.JSONDecodeError, OSError) as error:
        print(f"Warning: Could not load expenses: {error}")
        return []


# Save expenses to JSON file
def save_expenses(expenses):
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(expenses, file, indent=4, ensure_ascii=False)
        return True

    except OSError as error:
        print(f"Error saving expenses: {error}")
        return False


# Get a non-empty text value
def get_required_text(prompt):
    while True:
        value = input(prompt).strip()

        if value:
            return value

        print("This field cannot be empty. Please try again.")


# Validate amount
def get_valid_amount():
    while True:
        try:
            amount = float(input("Enter amount: Rs "))

            if not math.isfinite(amount):
                print("Amount must be a finite number.")
            elif amount <= 0:
                print("Amount must be greater than zero.")
            else:
                return amount

        except ValueError:
            print("Invalid input! Please enter a number.")


# Validate date
def get_valid_date():
    while True:
        date_input = input(
            "Enter date (YYYY-MM-DD): "
        ).strip()

        try:
            parsed_date = datetime.strptime(
                date_input, "%Y-%m-%d"
            )

            # Require the exact YYYY-MM-DD format
            if parsed_date.strftime("%Y-%m-%d") == date_input:
                return date_input

            print("Invalid date! Please use YYYY-MM-DD.")

        except ValueError:
            print("Invalid date! Please use YYYY-MM-DD.")


# Add a new expense
def add_expense(expenses):
    print("\n------- Add Expense -------")

    title = get_required_text("Enter expense title: ")
    category = get_required_text("Enter category: ")
    amount = get_valid_amount()
    date = get_valid_date()
    note = input("Enter note (optional): ").strip()

    expense = {
        "title": title,
        "category": category,
        "amount": amount,
        "date": date,
        "note": note
    }

    expenses.append(expense)

    if save_expenses(expenses):
        print("Expense added successfully!")
    else:
        # Remove the unsaved expense from memory
        expenses.pop()


# View all expenses
def view_expenses(expenses):
    if not expenses:
        print("No expenses found.")
        return

    print("\n------- All Expenses -------")

    for index, expense in enumerate(expenses, start=1):
        print(f"\nExpense {index}")
        print(f"Title: {expense.get('title', 'N/A')}")
        print(f"Category: {expense.get('category', 'N/A')}")

        try:
            amount = float(expense.get("amount", 0))
            print(f"Amount: Rs. {amount:.2f}")
        except (ValueError, TypeError):
            print("Amount: Invalid data")

        print(f"Date: {expense.get('date', 'N/A')}")
        print(f"Note: {expense.get('note', '')}")


# Show expense summary
def show_summary(expenses):
    if not expenses:
        print("No expenses found.")
        return

    try:
        total = sum(
            float(expense["amount"])
            for expense in expenses
        )
    except (KeyError, ValueError, TypeError):
        print("Cannot calculate summary: some expense data is invalid.")
        return

    average = total / len(expenses)

    print("\n------- Expense Summary -------")
    print(f"Total Expenses: Rs. {total:.2f}")
    print(f"Number of Expenses: {len(expenses)}")
    print(f"Average Expense: Rs. {average:.2f}")

    category_totals = {}

    for expense in expenses:
        category = expense.get("category", "Uncategorized")
        amount = float(expense["amount"])

        category_totals[category] = (
            category_totals.get(category, 0) + amount
        )

    print("\n------- Category-wise Summary -------")

    for category, amount in category_totals.items():
        print(f"{category}: Rs. {amount:.2f}")


# Filter expenses by category
def filter_by_category(expenses):
    if not expenses:
        print("No expenses found.")
        return

    category = get_required_text(
        "Enter category to filter: "
    )

    found = False

    print("\n------- Filtered Expenses -------")

    for expense in expenses:
        expense_category = expense.get("category", "")

        if expense_category.strip().casefold() == category.casefold():
            print(f"\nTitle: {expense.get('title', 'N/A')}")
            print(f"Category: {expense_category}")
            print(f"Amount: Rs. {float(expense['amount']):.2f}")
            print(f"Date: {expense.get('date', 'N/A')}")
            print(f"Note: {expense.get('note', '')}")
            found = True

    if not found:
        print("No expenses found in this category.")


# Delete an expense
def delete_expense(expenses):
    if not expenses:
        print("No expenses to delete.")
        return

    view_expenses(expenses)

    try:
        number = int(
            input("\nEnter expense number to delete: ")
        )

        if not 1 <= number <= len(expenses):
            print("Invalid expense number.")
            return

        removed = expenses.pop(number - 1)

        if save_expenses(expenses):
            print(
                f"Expense '{removed.get('title', 'N/A')}' "
                "deleted successfully!"
            )
        else:
            # Restore the expense if saving fails
            expenses.insert(number - 1, removed)

    except ValueError:
        print("Please enter a valid whole number.")


# Main menu
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

        choice = input("Enter your choice (1-6): ").strip()

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
