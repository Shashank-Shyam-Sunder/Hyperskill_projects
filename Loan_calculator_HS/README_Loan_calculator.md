# Loan Calculator

## Overview
This project provides tools for calculating various loan parameters. It includes both a basic version for simple calculations and an advanced version with more features, including command-line argument parsing and different payment types.

## Features

### Basic Version (`loan_calculator_basic.py`)
- Calculate the number of monthly payments needed to repay a loan
- Calculate the monthly payment amount for a given loan term
- Handle cases where the last payment might be smaller
- Simple division-based calculations without interest

### Advanced Version (`loan_calculator_advance.py`)
- Calculate different loan parameters:
  - Monthly payment amount (when principal, periods, and interest are provided)
  - Loan principal (when payment, periods, and interest are provided)
  - Number of months to repay (when principal, payment, and interest are provided)
- Support for two payment types:
  - Annuity payments (equal payments throughout the loan term)
  - Differentiated payments (payments that decrease over time)
- Command-line argument parsing for easy use
- Interest rate calculations
- Overpayment calculation (total interest paid)
- User-friendly output formatting (e.g., converting months to years and months)

## How It Works

### Basic Version
1. The user inputs the loan principal amount
2. The user selects a calculation mode:
   - "m" to calculate the number of monthly payments
   - "p" to calculate the monthly payment amount
3. Based on the mode, the program asks for additional information
4. The program performs the calculation and displays the result
5. For monthly payment calculations, it handles cases where the last payment might be smaller

### Advanced Version
1. The program accepts command-line arguments:
   - `--type`: Type of payment (annuity or differentiated)
   - `--principal`: Loan principal amount
   - `--payment`: Monthly payment amount
   - `--periods`: Number of months
   - `--interest`: Annual interest rate
2. Based on the provided arguments, it calculates the missing parameter
3. For annuity payments, it can calculate:
   - Monthly payment (if principal, periods, and interest are provided)
   - Loan principal (if payment, periods, and interest are provided)
   - Number of months (if principal, payment, and interest are provided)
4. For differentiated payments, it calculates monthly payments for each month
5. It also calculates and displays the overpayment (total interest paid)

## Usage Examples

### Basic Version
```
Enter the loan principle:
1000
What do you want to calculate?
type "m" - for number of monthly payments,
type "p" - for the monthly payment:
m
Enter the monthly payment:
150
It will take 7 months to repay the loan
```

### Advanced Version
```
python loan_calculator_advance.py --type=annuity --principal=1000000 --periods=60 --interest=10
Your monthly payment = 21248!
Your overpayment = 274880
```

```
python loan_calculator_advance.py --type=diff --principal=1000000 --periods=10 --interest=10
Month 1: payment is 108334
Month 2: payment is 107500
Month 3: payment is 106667
Month 4: payment is 105834
Month 5: payment is 105000
Month 6: payment is 104167
Month 7: payment is 103334
Month 8: payment is 102500
Month 9: payment is 101667
Month 10: payment is 100834
Overpayment: 45837
```

## Skills Demonstrated
- Financial calculations and formulas
- Command-line argument parsing with `argparse`
- Conditional logic and function definition
- Error handling
- User input processing
- Mathematical operations and rounding
- String formatting for user-friendly output

## Requirements
- Python 3.6 or higher
- `argparse` module (included in Python standard library)

You can install the required dependencies using:
```bash
pip install -r requirements_loan_calculator.txt
```