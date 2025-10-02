# calculate.py

"""
Functions for calculating totals and reports from expenses.
"""

from storage import load_expenses_from_json


def total_spent():
    """Calculate and display the total amount spent."""
    expenses = load_expenses_from_json()

    if not expenses:
        print("No expenses recorded yet.")
        return

    total = sum(expense["amount"] for expense in expenses)
    print(f"Total Spent: {total:.2f}")


def total_spent_by_category():
    """Calculate and display spending totals by category."""
    expenses = load_expenses_from_json()

    if not expenses:
        print("No expenses recorded yet.")
        return

    # Group by category
    category_totals = {}
    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category not in category_totals:
            category_totals[category] = 0
        category_totals[category] += amount

    print("\n=====   Spending By Category   =====")
    for category, total in category_totals.items():
        print(f" {category}: {total:.2f}")


def show_spending_report():
    """
    Display a formatted spending report including:
    - Total spending across all expenses
    - Spending broken down by category
    """
    print("====================================")
    print("           Spending Report          ")
    print("====================================")
    total_spent()
    total_spent_by_category()
