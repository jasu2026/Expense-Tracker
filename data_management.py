# data_management.py
import json
from expense import Expense

def get_user_input():
    amount = float(input("Enter the amount spent: "))
    description = input("Enter a brief description: ")
    category = input("Enter expense category (e.g., food, transportation, entertainment): ")
    return Expense(amount, description, category)

def save_expense_to_file(expense):
    with open('expenses.json', 'a') as file:
        json.dump(expense.__dict__, file)
        file.write('\n')

def read_expenses_from_file():
    expenses = []
    try:
        with open('expenses.json', 'r') as file:
            lines = file.readlines()
            for line in lines:
                data = json.loads(line)
                expenses.append(Expense(**data))
    except FileNotFoundError:
        pass
    return expenses