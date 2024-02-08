def main():
    while True:
        print("1. Enter Expense")
        print("2. View Monthly Summary")
        print("3. View Category-wise Expenditure")
        print("4. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            expense_entry = get_user_input()
            save_expense_to_file(expense_entry)
        elif choice == '2':
            monthly_expenses = monthly_summary(read_expenses_from_file())
            for month, total_expense in monthly_expenses.items():
                print(f"{month}: ${total_expense}")
        elif choice == '3':
            expense_tracker = ExpenseTracker()
            expense_tracker.expenses = read_expenses_from_file()
            category_expenses = expense_tracker.categorize_expenses()
            for category, expenses in category_expenses.items():
                print(f"{category}: {len(expenses)} expenses")
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
