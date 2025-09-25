# expense.py

"""
Expense module containing the Expense class. 
Represents a single expense with validation and formatting utilities.
"""

from datetime import datetime

class Expense:
    """Represents a single expense record with validation."""
    
    def __init__(self, amount: float, category: str, description: str, date: str = None):
        # Validate amount
        if amount <= 0:
            raise ValueError("Amount entered must be greater than zero.")
        
        #Validate date or use today's date
        if date:
            try:
                datetime.strptime(date, "%Y-%m-%d")
            except ValueError:
                raise ValueError("Date must be in YYYY-MM-DD format.")
        else:
            date = datetime.today().strftime("%Y-%m-%d")
        
        self.amount = amount
        self.category = category.strip()
        self.description = description.strip()
        self.date = date

    def __repr__(self):
        # Developer-friendly representation
        return f"Expense(amount={self.amount}, category='{self.category}', date='{self.date}')"
    
    def __str__(self):
        # User-friendly string repressentation for display.
        return f"{self.date} | {self.category} | ${self.amount:.2f} | {self.description or 'No description'}"
    
    def to_dict(self):
        """Convert to dictionary (for JSON storage later)."""
        return{

            "amount": self.amount,
            "category": self.category,
            "description": self.description,
            "date": self.date
        }