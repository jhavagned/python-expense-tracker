# Python Expense Tracker

A **command-line expense tracker** built in Python 3.
This project is designed to practice and demonstrate core programming concepts including:

- User input and validation
- Data structures (lists, dictionaries)
- File handling and persistence (JSON, CSV, SQLite in later phases)
- Reporting and data analysis
- Automated testing with `pytest`
- Clean code organization and documentation

---

## Features (current & planned)

- [x] Interactive CLI menu
- [x] Add expense (amount, category, description, date)
- [x] View all expenses
- [x] Input validation
- [x] Save and load data from JSON
- [ ] Reporting (totals, category summaries)
- [ ] SQLite database support (future)
- [ ] Unit tests with `pytest`

---

## Project Structure

python-expense-tracker/
|---- main.py # CLI entry point
|---- tracker.py # Expense operations (add/view)
|---- expense.py # Expense class
|---- storage.py # JSON persistence (save/load)
|---- expenses.json # Data file (auto-generated)
|---- README.md # Documentation
|\_\_\_\_ .gitignore #Ignore build and runtime files

---

## Requirements

- Python 3.9+ recommended
- No external dependencies for initial version

---

## Running the Project

Clone the repository and run:

```bash

git clone https://github.com/jhavagned/python-expense-tracker.git
cd python-expense-tracker
python3 main.py

```

---

## Example Usage

```text

====== Python Expense Tracker ======
1. Add Expense
2. View Expenses
3. Quit

Select an option (1-3)> 1
Enter amount: 10.50
Enter category: Food
Enter description (optional): Lunch
Enter date (YYYY-MM-DD) or leave blank for today: 2025-09-29
Expense added successfully!

```

---

## License

This project is licensed under the MIT License -- see the [LICENSE](LICENSE) file for details.
