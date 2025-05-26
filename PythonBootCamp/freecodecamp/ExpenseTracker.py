'''
In this project, you're going to build a simple, yet functional expense tracker in Python.

1. Start by defining a function named add_expense that takes three parameters: expenses, amount and category.
2. Define a function named print_expenses that takes one parameter expenses. This function will later be used to display each expense in your list.
3. Define a function named total_expenses that takes one parameter expenses.
4. Within the filter_expenses_by_category function. Use expense as the parameter and evaluate the comparison between the value of the 'category' key of the expense dictionary and category using the equality operator.
5. Define a function named main without parameters. Fill the function body with the expenses list you created at the beginning of this project. You will use this list to store the expense records.
    -
'''

def add_expense(expenses, amount, category):
    expenses.append({'amount': amount, 'category': category})

def print_expenses(expenses):
    for expense in expenses:
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')

def total_expenses(expenses):
    return sum(map(lambda expense: expense['amount'], expenses))

def filter_expenses_by_category(expenses, category):
    return filter(lambda expense: expense['category'] == category, expenses)

def _main_():
    expenses = []
    while True:
        print('\nEnpense Tracker')
        print('1. Add an expense: ')
        print('2. List all expenses: ')
        print('3. Show total expenses: ')
        print('4. Filter expenses by category: ')
        print('5. Exit!!!')

        choice = input('\nEnter your choice: ')
        if choice == '1':
            amount = float(input('Enter amount: '))
            category = input('\nEnter category: ')
            add_expense(expenses, amount, category)
        elif choice == '2':
            print_expenses(expenses)
        elif choice == '3':
            print('\nTotal expenses: ', total_expenses(expenses))
        elif choice == '4':
            category = input('\nEnter category to filter: ')
            print(f'Expenses for {category}: ')
            output = filter_expenses_by_category(expenses, category)
            print_expenses(output)
        elif choice == '5':
            print('Exiting the program.')
            break
        else:
            raise ValueError(f'Invalid choice: ${choice}')
