# tracker.py

"""
Tracker module for managing expenses.
Provides functions to add and view expenses.
"""

from expense import Expense
from storage import save_expenses_to_json, load_expenses_from_json
from tabulate import tabulate

# Temporary in-memory list to store expenses
expenses = load_expenses_from_json()

if not expenses:
    print("No expenses found. Startig with an empty tracker.")


def add_expense():
    """Prompt the user for expense details and add an Expense object to the list."""
    amount_input = input("Enter amount: ").strip()
    if not amount_input:
        print("Amount cannot be blank.")
        return

    try:
        amount = float(amount_input)
    except ValueError:
        print(f"Could not convert '{amount_input}' to float. Invalid format.")
        return

    category = input("Enter category: ").strip()
    if not category:
        print("Category cannot be blank.")
        return

    description = input("Enter description (optional): ")
    date = input(
        "Enter date (YYYY-MM-DD) or leave blank for today: ").strip() or None

    try:
        expense = Expense(amount, category, description, date)
        expenses.append(expense.to_dict())
        save_expenses_to_json(expenses)
        print("Expense added successfully!")
    except ValueError as e:
        print(f"Error: {e}")


def view_expenses():
    """Display all recorded expenses"""
    if not expenses:
        print("No available expenses at the moment.")
        return

    # Convert expense dicts into rows
    table_data = [[i+1, e['date'], e['category'],
                   f"${e['amount']:.2f}", e['description'] or "No description"] for i, e in enumerate(expenses)]

    headers = ["#", "Date", "Category", "Amount", "Description"]
    print(tabulate(table_data, headers=headers, tablefmt="grid"))
