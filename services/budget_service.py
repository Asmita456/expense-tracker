
import json
from pathlib import Path
from datetime import date

from utils.validators import get_valid_amount

BUDGET_FILE = (
    Path(__file__).resolve().parent.parent
    / "data"
    / "budgets.json"
)


def load_budgets():
    if not BUDGET_FILE.exists():
        return {}

    try:
        with open(BUDGET_FILE, "r", encoding="utf-8") as file:
            budgets = json.load(file)

        if isinstance(budgets, dict):
            return budgets

        print("Warning: Invalid budget data format.")
        return {}

    except (json.JSONDecodeError, OSError) as error:
        print(f"Warning: Could not load budgets: {error}")
        return {}


def save_budgets(budgets):
    try:
        BUDGET_FILE.parent.mkdir(parents=True, exist_ok=True)

        with open(BUDGET_FILE, "w", encoding="utf-8") as file:
            json.dump(budgets, file, indent=4)

        return True

    except OSError as error:
        print(f"Error saving budgets: {error}")
        return False


def set_monthly_budget(budgets):
    month = input(
        "Enter month (YYYY-MM), e.g. 2026-10: "
    ).strip()

    try:
        date.fromisoformat(month + "-01")
    except ValueError:
        print("Invalid month! Please use YYYY-MM.")
        return

    print(f"Set budget for {month}")
    amount = get_valid_amount()

    old_budget = budgets.get(month)
    budgets[month] = amount

    if save_budgets(budgets):
        print(f"Monthly budget set: Rs. {amount:.2f}")
    else:
        if old_budget is None:
            budgets.pop(month, None)
        else:
            budgets[month] = old_budget


def show_monthly_budget(budgets, expenses):
    month = input(
        "Enter month (YYYY-MM), e.g. 2026-10: "
    ).strip()

    try:
        date.fromisoformat(month + "-01")
    except ValueError:
        print("Invalid month! Please use YYYY-MM.")
        return

    budget = budgets.get(month)

    if budget is None:
        print(f"No budget set for {month}.")
        return

    total_spent = 0.0

    for expense in expenses:
        expense_date = expense.get("date", "")

        if expense_date.startswith(month):
            try:
                amount = float(expense.get("amount", 0))
                if amount > 0:
                    total_spent += amount
            except (ValueError, TypeError):
                continue

    remaining = float(budget) - total_spent

    print(f"\n===== BUDGET REPORT: {month} =====")
    print(f"Monthly Budget: Rs. {float(budget):.2f}")
    print(f"Total Spent:    Rs. {total_spent:.2f}")
    print(f"Remaining:      Rs. {remaining:.2f}")

    if remaining < 0:
        print(
            f"WARNING: Budget exceeded by Rs. "
            f"{abs(remaining):.2f}!"
        )
    elif remaining == 0:
        print("You have used your entire budget.")
    else:
        print("You are within your monthly budget.")
