Expense Tracker (Python CLI)

A command-line expense tracker built in Python that helps users manage income and expenses, calculate balances, and generate financial summaries by category, month, and year.

The application uses structured data storage and date-based filtering to provide clear financial insights through an interactive CLI menu.

✨ Features

- Record expenses with:
  - Amount
  - Category
  - Date (YYYY-MM-DD)
- Record income with:
  - Amount
  - Source
  - Date
- View all stored expenses and income
- Calculate:
  - Total expenses per category
  - Total income per source
  - Overall balance (income minus expenses)
- Filter income and expenses by:
  - Month
  - Year
- Interactive command-line menu for easy navigation

🧱 Tech Stack

- Python 3
- collections.defaultdict for efficient data aggregation
- datetime for date parsing and filtering
- pprint for readable CLI output formatting

📁 Data Model
Expenses and income are stored as dictionaries where:
- Each category or source maps to a list of transactions
- Each transaction contains:
  - amount
  - date

Example structure:
expenses = {
  "food": [
    {"amount": 25.5, "date": "2024-03-10"},
    {"amount": 12.0, "date": "2024-03-15"}
  ]
}

▶️ Running the Application

1. Clone the repository
2. Run the Python file
3. Follow the on-screen menu to interact with the tracker

🖥️ CLI Menu Options
1. View income
2. View expenses
3. View balance
4. View income and expenses per month
5. View income and expenses per year
6. Exit the application
