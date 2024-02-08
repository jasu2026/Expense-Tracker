# expense.py

class Expense:
    def __init__(self, amount, description, category):
        self.amount = amount
        self.description = description
        self.category = category


# user_interface.py
from data_management import get_user_input, save_expense_to_file, read_expenses_from_file
from expense_tracker import ExpenseTracker, monthly_summary

