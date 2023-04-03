import pandas as pd
from tabulate import tabulate

def add_expense(amount, category, date):
    with open('expenses.csv', 'a') as f:
        f.write(f"{date},{category},{amount}\n")
    print("Expense added successfully")

def show_report():
    df = pd.read_csv('expenses.csv', names=['Date', 'Category', 'Amount'])
    report = df.groupby(['Category'], as_index=False).sum()
    print(tabulate(report, headers=['Category', 'Amount'], tablefmt='fancy_grid'))

add_expense(100, 'Groceries', '2023-04-01')
add_expense(50, 'Transportation', '2023-04-02')
add_expense(200, 'Entertainment', '2023-04-03')
show_report()
