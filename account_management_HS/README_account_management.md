# Account Management

## Overview
Account Management is a simple shop accounting system that tracks item prices, calculates total income, and determines net income after expenses. It's designed to help shop owners manage their financial records and calculate profitability.

## Features
- Store and display shop items with their prices
- Track earnings for each item
- Calculate total income from all items
- Input and track expenses (staff and other expenses)
- Calculate net income (total income minus expenses)
- Formatted output for financial data

## How It Works
The program operates in three main stages:

1. **Price Listing**:
   - Stores shop items and their prices in a dictionary
   - Displays the prices of all items in a formatted list

2. **Income Calculation**:
   - Tracks earnings for each item in a separate dictionary
   - Calculates and displays the total income from all items

3. **Expense Management and Net Income**:
   - Takes user input for staff expenses
   - Takes user input for other expenses
   - Calculates net income by subtracting expenses from total income
   - Displays the final net income

## Usage Example
```
Prices:
Bubblegum: $2
Toffee: $0.2
Ice cream: $5
Milk chocolate: $4
Doughnut: $2.5
Pancake: $3.2

Earned amount:
Bubblegum: $202
Toffee: $118
Ice cream: $2250
Milk chocolate: $1680
Doughnut: $1075
Pancake: $80

Income: $5405
Staff expenses: 1150
Other expenses: 300
Net income: $3955
```

## Skills Demonstrated
- Dictionary data structures for storing key-value pairs
- Iteration through dictionaries using for loops
- String formatting with f-strings
- User input for data collection
- Basic arithmetic operations for financial calculations
- Financial data organization and presentation

## Applications
This program can be used by:
- Small shop owners to track daily sales and expenses
- Entrepreneurs to calculate profitability
- Students learning financial accounting concepts
- Anyone needing a simple system to track income and expenses

## Requirements
- Python 3.6 or higher

You can install the required dependencies using:
```bash
pip install -r requirements_account_management.txt
```

## Potential Enhancements
- Save data to files for persistent storage
- Add date tracking for income and expenses
- Implement multiple time period reporting (daily, weekly, monthly)
- Add data visualization for financial trends
- Create a more interactive user interface