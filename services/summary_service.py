
def show_summary(expenses):
    if not expenses:
        print("No expenses found.")
        return

    try:
        amounts = [float(expense["amount"]) for expense in expenses]
    except (KeyError, ValueError, TypeError):
        print("Cannot calculate summary: some expense data is invalid.")
        return

    total = sum(amounts)
    average = total / len(expenses)

    print("\n------- Expense Summary -------")
    print(f"Total Expenses: Rs. {total:.2f}")
    print(f"Number of Expenses: {len(expenses)}")
    print(f"Average Expense: Rs. {average:.2f}")

    category_totals = {}

    for expense, amount in zip(expenses, amounts):
        category = expense.get("category", "Uncategorized")

        category_totals[category] = (
            category_totals.get(category, 0) + amount
        )

    print("\n------- Category-wise Summary -------")

    for category, amount in category_totals.items():
        print(f"{category}: Rs. {amount:.2f}")
