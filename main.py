
from services.expense_service import (
    load_expenses,
    add_expense,
    view_expenses,
    filter_by_category,
    delete_expense,
)
from services.summary_service import show_summary
from services.budget_service import (
    load_budgets,
    set_monthly_budget,
    show_monthly_budget,
)


def main():
    expenses = load_expenses()
    budgets = load_budgets()

    while True:
        print("\n===== EXPENSE TRACKER =====")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Show Expense Summary")
        print("4. Filter by Category")
        print("5. Delete Expense")
        print("6. Set Monthly Budget")
        print("7. View Monthly Budget")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ").strip()

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
            set_monthly_budget(budgets)

        elif choice == "7":
            show_monthly_budget(budgets, expenses)

        elif choice == "8":
            print("Thank you for using Expense Tracker!")
            break

        else:
            print("Invalid choice. Please select 1-8.")


if __name__ == "__main__":
    main()
