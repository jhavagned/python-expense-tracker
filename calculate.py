# calculate.py

"""
Functions for calculating totals and reports from expenses.
"""

from storage import load_expenses_from_json
from tabulate import tabulate


def total_spent():
    """Calculate and display the total amount spent."""
    expenses = load_expenses_from_json()
    return sum(expense["amount"] for expense in expenses) if expenses else 0.0


def total_spent_by_category():
    """Calculate and display spending totals by category."""
    expenses = load_expenses_from_json()
    if not expenses:
        return {}

    # Group by category
    category_totals = {}
    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]
        category_totals[category] = category_totals.get(category, 0) + amount

    return category_totals


def show_spending_report():
    """
    Display a formatted spending report including:
    - Total spending across all expenses
    - Spending broken down by category
    """

    expenses = load_expenses_from_json()
    if not expenses:
        print("No expenses recorded yet.")
        return

    print("\n====================================")
    print("           Spending Report          ")
    print("====================================\n")

    # Show total
    total = total_spent()
    total_table = [["Total Spent", f"${total:.2f}"]]
    print(tabulate(total_table, headers=["", "Value"], tablefmt="grid"))
    print()

    # Show categoriess
    category_totals = total_spent_by_category()
    category_table = [[cat, f"${amt:.2f}"]
                      for cat, amt in category_totals.items()]
    print(tabulate(category_table, headers=[
          "Category", "Total Spent"], tablefmt="grid"))
