# storage.py

import json
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

EXPENSES_FILE = os.getenv("EXPENSES_FILE", os.path.join(
    os.path.dirname(__file__), "expenses.json"))


def save_expenses_to_json(expenses, file_path=EXPENSES_FILE):
    """Save expenses list to a JSON file."""
    try:
        with open(file_path, 'w', encoding="utf-8") as file:
            json.dump(expenses, file, indent=4)
    except (FileNotFoundError, PermissionError, TypeError) as e:
        print(f"Error saving expenses: {e}")


def load_expenses_from_json(file_path=EXPENSES_FILE):
    """Load expenses from JSON file, return list."""
    try:
        if os.path.exists(file_path):
            with open(EXPENSES_FILE, "r", encoding="utf-8") as file:
                return json.load(file)
    except (FileNotFoundError, PermissionError, json.JSONDecodeError) as e:
        print(f"Error loading expenses: {e}")
    return []
