# expense_tracker.py
from expense import Expense

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def categorize_expenses(self):
        categories = {}
        for expense in self.expenses:
            if expense.category in categories:
                categories[expense.category].append(expense)
            else:
                categories[expense.category] = [expense]
        return categories

def monthly_summary(expenses):
    monthly_expenses = {}
    for expense in expenses:
        month = expense.date.strftime("%Y-%m")
        if month in monthly_expenses:
            monthly_expenses[month] += expense.amount
        else:
            monthly_expenses[month] = expense.amount
    return monthly_expenses