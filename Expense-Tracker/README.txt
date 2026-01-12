Expense Tracker

A simple Python-based Expense Tracker that allows you to add, view, and analyze expenses by category and month. This project is designed to help you track spending and practice Python programming with dictionaries, loops, and datetime handling.

Features

Add Expenses: Add an expense with amount, category, and date.

View Expenses: See all recorded expenses organized by category.

Total per Category: Calculate total expenses for each category.

Filter by Month: Calculate total expenses per category for a specific month.

Data Structure

Expenses are stored in a nested dictionary format:

{
    "food": [
        {"amount": 25.50, "date": "2026-01-07"},
        {"amount": 10.00, "date": "2026-01-20"}
    ],
    "transport": [
        {"amount": 15.00, "date": "2026-01-10"}
    ]
}


Category → key (e.g., "food", "transport")

Value → list of expense dictionaries with amount and date

This structure allows easy aggregation and filtering.

How to Use
from collections import defaultdict
from datetime import datetime
from expense_tracker import Solution  # Assuming your class is in expense_tracker.py

# Initialize expense tracker
tracker = Solution()

# Add expenses
tracker.add_expense(amount=25.50, category="food", date="2026-01-07")
tracker.add_expense(amount=10.00, category="food", date="2026-01-20")
tracker.add_expense(amount=15.00, category="transport", date="2026-01-10")

# View all expenses
print(tracker.view())

# Get total per category
print(tracker.total())

# Filter expenses for a specific month (e.g., March)
print(tracker.month_filter(target_month=3, target_year=2026))

Project Goals

Learn Python data structures like dictionaries and defaultdict.

Practice iterating and aggregating nested data.

Use Python’s datetime module to handle and filter dates.

Build a small, useful project suitable for a portfolio or resume.

Future Improvements

Add yearly totals or comparison between months.

Export expenses to CSV for record keeping.

Add a CLI menu for easier interaction.

Include visualizations with matplotlib or seaborn.