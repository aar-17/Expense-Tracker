from datetime import date
import json
import pickle

FILENAME = "expenses.json"
PICKLEFILENAME = "expensespickle.pkl"

def exportexpenses():
    if not expenses:
        print("No expenses recorded to export.")
        return
    try:
        with open(PICKLEFILENAME, 'wb') as pklfile:
            pickle.dump(expenses, pklfile) 
            
        print(f"\nSuccessfully exported {len(expenses)} expenses to {PICKLEFILENAME}") 
    except Exception as e:
        print(f"Error during pickle export: {e}")

def load_expenses():
    global expenses
    try:
        with open(FILENAME, 'r') as f:
            expenses = json.load(f)
        print(f"Loaded {len(expenses)} expenses from {FILENAME}.")
    except FileNotFoundError:
        print("No existing expense file found. Starting fresh.")
        expenses = []
    except json.JSONDecodeError:
        print("Error reading JSON file. Starting fresh.")
        expenses = []

def save_expenses():
    try:
        with open(FILENAME, 'w') as f:
            json.dump(expenses, f, indent=4) 
        print(f"Data saved successfully to {FILENAME}.")
    except Exception as e:
        print(f"Error saving data: {e}")

expenses = []

def add_expense(date, amount, category, description):
    if amount <= 0:
        print("Error: Invalid amount.")
        return
      
    expense = {
        "date": date.today().strftime("%d-%B-%Y"),
        "amount": amount,
        "category": category.capitalize(),
        "description": description
    }
    expenses.append(expense)
    print(f"Added: {category} - ${amount:.2f}")

def view_summary():
    if not expenses:
        print("No expenses recorded yet.")
        return

    total_spent = 0.0
    category_totals = {}

    print("\n" + "="*30)
    print("       EXPENSE SUMMARY ")
    print("="*30)

    for expense in expenses:
        amount = expense['amount']
        category = expense['category']
        total_spent += amount

        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount

    print(f"\n--- Summary by Category  ---")
    today = date.today()
    dateform = today.strftime("%d-%B-%Y")
    print(f"\n--- {dateform}  ---")
    for category, total in category_totals.items():
        percentage = (total / total_spent) * 100
        print(f"\n* {category:<10}: ${total:>8.2f} ({percentage:.1f}%)")

    print("-" * 30)
    print(f"** TOTAL SPENT: ${total_spent:>.2f} **")
    print("-" * 30)

def descriptions():
    for expense in expenses:
        description = expense['description']
        description_totals = {}
        if description in description_totals:
            description_totals[description] += description
        else:
            description_totals[description] = description

        print(f"---  Description for expenses  ---\n {description}")

def main():
    print(" Welcome to Expense Tracker ")
    load_expenses()

    while True:
        print("\n--- Menu ---")
        print("1. **Add** a new expense")
        print("2. **View** expense summary")
        print("3. **View** expense descriptions")
        print("4. **Export** to pickle")
        print("5. **Exit**")
        
        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':
                amount = float(input("Enter amount spent ($): "))
                category = input("Enter category (e.g., Food, Travel, Rent, etc.): ")
                description = input("Enter a brief description: ")
                add_expense(date, amount, category, description)
                save_expenses()

        elif choice == '2':
            view_summary()

        elif choice == '3':
            descriptions()

        elif choice == '4':
            exportexpenses()
        
        elif choice == '5':
            print("Thank you for tracking your expenses. Goodbye!")
            save_expenses()
            break
        
        else:
            print("Invalid choice. Please select 1, 2, 3, 4 or 5.")

if __name__ == "__main__":
    main()