
import json
from pathlib import Path

from utils.validators import (
    get_required_text,
    get_valid_amount,
    get_valid_date,
)

DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "expenses.json"


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


def save_expenses(expenses):
    try:
        DATA_FILE.parent.mkdir(parents=True, exist_ok=True)

        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(expenses, file, indent=4, ensure_ascii=False)

        return True

    except OSError as error:
        print(f"Error saving expenses: {error}")
        return False


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
        "note": note,
    }

    expenses.append(expense)

    if save_expenses(expenses):
        print("Expense added successfully!")
    else:
        expenses.pop()


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


def filter_by_category(expenses):
    if not expenses:
        print("No expenses found.")
        return

    category = get_required_text("Enter category to filter: ")
    found = False

    print("\n------- Filtered Expenses -------")

    for expense in expenses:
        expense_category = expense.get("category", "")

        if expense_category.strip().casefold() == category.casefold():
            print(f"\nTitle: {expense.get('title', 'N/A')}")
            print(f"Category: {expense_category}")

            try:
                amount = float(expense["amount"])
                print(f"Amount: Rs. {amount:.2f}")
            except (ValueError, TypeError, KeyError):
                print("Amount: Invalid data")

            print(f"Date: {expense.get('date', 'N/A')}")
            print(f"Note: {expense.get('note', '')}")
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
            expenses.insert(number - 1, removed)

    except ValueError:
        print("Please enter a valid whole number.")
