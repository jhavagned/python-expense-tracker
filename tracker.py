# tracker.py

"""
Tracker module for managing expenses.
Provides functions to add and view expenses.
"""

from expense import Expense

# Temporary in-memory list to store expenses
expenses = []

def add_expense():
    """Prompt the user for expense details and add an Expense object to the list."""
    amount_input = input("Enter amount: ").strip()
    if not amount_input:
        print("Amount cannot be blank.")
        return
    
    try:
        amount = float(amount_input)
    except:
        print("Ivalid number entered.")
        return
    
    category = input("Enter category: ").strip()
    if not category:
        print("Category cannot be blank.")
        return
    
    description = input("Enter description (optional): ")
    date = input ("Enter date (YYYY-MM-DD) or leave blank for today: ").strip() or None

    try:
        expense = Expense(amount, category, description, date)
        expenses.append(expense)
        print("Expense added successfully!")
    except ValueError as e:
        print(f"Error: {e}")

def view_expenses():
    """Display all recorded expensses in a formatted list."""
    if not expenses:
        print("No available expenses at the moment.")
    else: 
        for i, expense in enumerate(expenses, 1):
            print(f"{i}. {expense}")