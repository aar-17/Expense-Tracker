# Expense-Tracker

# Overview of the project
This Python script implements a simple console-based Expense Tracker designed to help a user record, manage, summarize, and save their daily spending.
​The project utilizes standard Python libraries (json, pickle, and datetime) to handle data persistence and time management.
​  Key Features
​1. Data Management and Persistence
​Loading: Expenses are loaded automatically upon startup from a JSON file (expenses.json). If the file is missing or corrupted, the program starts with an empty list.
​Saving: All recorded expenses are automatically saved to expenses.json after every new addition and upon exiting the program, ensuring data is retained across sessions.
​Exporting: A dedicated function allows the user to export the current list of expenses to a binary format using Python's pickle module (expensespickle.pkl), providing a simple backup mechanism.
​2. Expense Tracking
​Adding Expenses: The user can quickly input the amount, category (e.g., Food, Transport), and a brief description for any expenditure.
​Automatic Timestamp: The current date is automatically captured and recorded with each new expense.
​3. Reporting and Analysis
​Summary View (view_summary): This is the core analytical feature. It calculates and displays:
​The total amount spent across all records.
​The total amount spent per category.
​The percentage breakdown of spending for each category relative to the total spent.
​Detailed View (descriptions): This function lists every recorded expense in detail, showing the date, amount, category, and description, offering a clear log of all transactions.

# Features
The expense tracker code provides several key features centered around data management, user interaction, and basic financial reporting.
​Here is a breakdown of the specific features implemented in your Python code:
​I. Core Expense Management
​Expense Recording (add_expense)
​Allows the user to input the amount, category, and description of a new expense.
​Input Validation: Ensures the entered amount is positive (amount > 0).
​Data Standardization: Automatically capitalizes the first letter of the category for consistent reporting (e.g., food becomes Food).
​Automatic Timestamping: Records the current date using date.today() and formats it clearly (dd-Month-YYYY).
​Summary Reporting (view_summary)
​Total Spent Calculation: Aggregates and displays the grand total of all expenses recorded.
​Category Aggregation: Calculates the sum of spending for each unique category (e.g., total spent on Food, total spent on Travel).
​Percentage Breakdown: Shows the proportion (percentage) of total spending that each category represents.
​Detailed Listing (descriptions)
​Provides a straightforward, tabular view of every single transaction, including the date, amount, category, and description, acting as a complete transaction log.
​II. Data Persistence and Backup
​JSON Data Storage (load_expenses, save_expenses)
​Automatic Loading: Attempts to load existing expense data from expenses.json upon starting the program.
​Error Handling (Loading): Gracefully handles two common errors:
​FileNotFoundError: Starts fresh if the file doesn't exist.
​json.JSONDecodeError: Starts fresh if the file is corrupted or empty.
​Automatic Saving: Saves the current state of the expenses list back to expenses.json (formatted with indent=4) after every new expense and upon program exit.
​Pickle Export for Backup (exportexpenses)
​Provides an option to export all current expense data to a binary file (expensespickle.pkl) using the pickle module. This is useful for creating a quick, complete data backup.
​III. User Interface and Navigation
​Interactive Menu (main)
​Presents a clear, numbered menu to the user:
​Add a new expense
​View expense summary
​View expense descriptions
​Export to pickle
​Exit
​Input Handling: Takes user input and executes the corresponding function.
​Exit Functionality: Cleans up by calling save_expenses() before terminating the program.
​Looping: Keeps the application running until the user explicitly chooses to exit (choice 5).

# Technologies/tools used
•	Python language
•	VS code
•	Modules

# Steps to install & run the project
•	Install Python 
•	SetUp VS code 
•	Create File name expense.py
•	Write Code and Save it 
•	Execute the Code and record the output

# Instructions for testing
Quick Testing Instructions
​Initial Run:
​Start the script (python tracker.py).
​Verify it loads existing data or confirms a fresh start.
​Core Feature Check (CRUD):
​Add (Choice 1): Enter 3 expenses with different categories (e.g., Food, Travel). Verify the amounts are positive.
​Save Check: Confirm expenses.json is created/updated after adding.
​Reporting Check:
​Summary (Choice 2): Check that the Total Spent is accurate and that categories (e.g., Food and Travel) are correctly grouped, totaled, and their percentages are displayed.
​Detail View (Choice 3): Verify all 3 added expenses are listed completely in the detailed view.
​Persistence and Backup:
​Export (Choice 4): Confirm expensespickle.pkl is created.
​Exit (Choice 5): Exit the program and run it again.
​Reload Check: Verify the script prints "Loaded 3 expenses" (or similar) upon restart, confirming data loaded correctly.
​Error Handling:
​Attempt to add an expense with a negative or zero amount to confirm it is rejected.
​Enter an invalid menu choice (e.g., '6') to check the error message.

