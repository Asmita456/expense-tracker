
# Expense Tracker

## Project Description
Expense Tracker is a Python-based command-line application that helps users record, view, filter, summarize, and manage daily expenses. It stores data in JSON files, so no database is required.

## Features
- Add new expenses
- View all expenses
- Calculate total and average expenses
- View category-wise expense summaries
- Filter expenses by category
- Delete expenses
- Validate expense amounts and dates
- Set a monthly budget
- View monthly budget reports
- Calculate total monthly spending and remaining budget
- Warn users when they exceed their monthly budget
- Store expense and budget data in JSON files

## Technologies Used
- Python
- JSON
- Visual Studio Code
- Git and GitHub

## Project Structure

```text
expense-tracker/
├── data/
│   ├── expenses.json
│   └── budgets.json
├── services/
│   ├── __init__.py
│   ├── expense_service.py
│   ├── summary_service.py
│   └── budget_service.py
├── utils/
│   ├── __init__.py
│   └── validators.py
├── main.py
├── .gitignore
└── README.md
```

## Requirements
- Python 3 installed
- Visual Studio Code or any text editor
- Git (optional, for version control)

## How to Run
1. Clone or download the project.
2. Open the project folder in VS Code.
3. Open the terminal in the project folder.
4. Run the following command:

   ```bash
   python main.py
   ```

## Available Menu Options
1. Add Expense
2. View All Expenses
3. Show Expense Summary
4. Filter by Category
5. Delete Expense
6. Set Monthly Budget
7. View Monthly Budget
8. Exit

## Data Storage
Expense records are stored in `data/expenses.json`, and monthly budgets are stored in `data/budgets.json`.

The application uses JSON files to preserve data between program runs.

## Input Validation
The application validates expense amounts and dates to help prevent invalid input. Monthly budgets are organized by month using the `YYYY-MM` format, such as `2026-10`.

## Future Improvements
- Edit existing expenses
- Display monthly spending charts
- Export expense reports to CSV
- Add a graphical user interface
- Add automated tests

## Author
Asmita Pandeya
