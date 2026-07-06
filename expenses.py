import datetime

class Expense:
    def __init__(self, date: str, amount: float, category: str, description: str):
        self.date = self.validate_date(date)
        self.amount = self.validate_amount(amount)
        self.category = self.validate_string(category, "Category")
        self.description = self.validate_string(description, "Description")

    @staticmethod
    def validate_date(date_str: str) -> str:
        try:
            datetime.datetime.strptime(date_str, "%Y-%m-%d")
            return date_str
        except ValueError:
            raise ValueError("Invalid date format. Use YYYY-MM-DD.")

    @staticmethod
    def validate_amount(amount: float) -> float:
        try:
            val = float(amount)
            if val <= 0:
                raise ValueError("Amount must be greater than zero.")
            return val
        except (ValueError, TypeError):
            raise ValueError("Amount must be a valid positive number.")

    @staticmethod
    def validate_string(text: str, field_name: str) -> str:
        if not text or not str(text).strip():
            raise ValueError(f"{field_name} cannot be empty.")
        return str(text).strip()

    def to_dict(self) -> dict:
        return {
            "date": self.date,
            "amount": self.amount,
            "category": self.category,
            "description": self.description
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(data["date"], data["amount"], data["category"], data["description"])


class ExpenseManager:
    def __init__(self):
        self.expenses = []
        self.budgets = {}

    def add_expense(self, expense: Expense) -> str:
        self.expenses.append(expense)
        if expense.category in self.budgets:
            total_spent = sum(e.amount for e in self.expenses if e.category == expense.category)
            if total_spent > self.budgets[expense.category]:
                return f"Warning: You have exceeded your budget for {expense.category}!"
        return "Expense added successfully."

    def remove_expense(self, index: int) -> bool:
        if 0 <= index < len(self.expenses):
            self.expenses.pop(index)
            return True
        return False

    def search_expenses(self, query: str, category: str = None):
        results = []
        for e in self.expenses:
            match_query = query.lower() in e.description.lower() or query.lower() in e.category.lower()
            match_cat = category is None or e.category.lower() == category.lower()
            if match_query and match_cat:
                results.append(e)
        return results

    def set_budget(self, category: str, amount: float):
        if amount < 0:
            raise ValueError("Budget must be positive.")
        self.budgets[category.strip()] = float(amount)