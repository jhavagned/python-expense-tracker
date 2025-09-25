# Python Expense Tracker

A **command-line expense tracker** built in Python 3. 
This project is designed to practice and demonstrate core programming concepts including:

- User input and validation
- Data structures (lists, dictionaries)
- File handling and persistence (JSON, CSV, SQLite in later phases)
- Reporting and data analysis
- Unit testing with `pytest`
- Clean code organization and documentation


---


## Features (current & planned)

- [x] Interactive CLI menu
- [x] Add expense (amount, category, description, date)
- [x] View all expenses
- [x] Input validation
- [ ] Save and load data from JSON
- [ ] Reporting (totals, category summaries)
- [ ] SQLite database support (future)
- [ ] Unit tests with `pytest`


---


## Project Structure

python-expense-tracker/
|---- main.py # CLI entry point
|---- tracker.py # Expense operations (add/view)
|---- expense.py # Expense class
|---- README.md # Documentation
|____ .gitignore #Ignore build/runtime files


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


## License

This project is licensed under the MIT License -- see the [LICENSE](LICENSE) file for details.
