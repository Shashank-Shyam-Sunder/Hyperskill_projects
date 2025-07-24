# Simple Calculator

## Overview
Simple Calculator is a Python program that performs basic arithmetic operations on two numbers. It takes user input for the numbers and the desired operation, then calculates and displays the result.

## Features
- Addition (+)
- Subtraction (-)
- Multiplication (*)
- Division (/)
- Modulus (mod) - remainder after division
- Power (pow) - exponentiation
- Integer division (div) - division that results in a whole number
- Error handling for division by zero

## How It Works
1. The program prompts the user to enter the first number
2. The user is then asked to enter the second number
3. Next, the user selects an arithmetic operation from the available options
4. The program performs the selected operation on the two numbers
5. The result is displayed to the user
6. If the user attempts to divide by zero, the program handles the error and displays an appropriate message

## Usage Example
```
Enter first number: 5
Enter second number: 2
Enter arithmetic operation: +
7.0

Enter first number: 10
Enter second number: 3
Enter arithmetic operation: mod
1.0

Enter first number: 8
Enter second number: 0
Enter arithmetic operation: /
Division by 0!
```

## Supported Operations
| Operation | Symbol | Description | Example |
|-----------|--------|-------------|---------|
| Addition | + | Adds two numbers | 5 + 3 = 8 |
| Subtraction | - | Subtracts second number from first | 5 - 3 = 2 |
| Multiplication | * | Multiplies two numbers | 5 * 3 = 15 |
| Division | / | Divides first number by second | 5 / 3 = 1.6667 |
| Modulus | mod | Returns remainder after division | 5 mod 3 = 2 |
| Power | pow | Raises first number to power of second | 5 pow 3 = 125 |
| Integer Division | div | Division with result rounded down | 5 div 3 = 1 |

## Skills Demonstrated
- Function definition and calling
- User input handling
- Type conversion (string to float)
- Conditional statements (if-elif-else)
- Exception handling with try-except
- Basic arithmetic operations
- Return values from functions

## Requirements
- Python 3.6 or higher

You can install the required dependencies using:
```bash
pip install -r requirements_simple_calculator.txt
```