# main.py

"""
Main entry point for the Python Expense Tracker CLI application.
Handles the user interface loop and delegates functionality to 
tracker.py.
"""

from tracker import add_expense, view_expenses
from calculate import show_spending_report


def main():
    """Run the main CLI menu loop."""

    while True:
        print("\n====== Python Expense Tracker ======")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Show Expense Report")
        print("4. Quit")

        choice = input("Select an option (1-3)>")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            show_spending_report()
        elif choice == "4":
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
