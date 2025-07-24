# Bill Splitter

## Overview
Bill Splitter is a Python application that helps divide a bill among a group of friends. It includes a special "Who is lucky?" feature that randomly selects one person who doesn't have to pay, with their portion being split among the others.

## Features
- Input the number of friends joining for the bill
- Enter each friend's name
- Enter the total bill amount
- Split the bill equally among all friends
- Optional "Who is lucky?" feature to randomly select one person who doesn't have to pay
- Recalculate shares when a lucky person is selected

## How It Works
1. The program asks for the number of friends joining (including you)
2. If the number is valid (greater than 0), it prompts for each friend's name
3. It then asks for the total bill value
4. The bill is initially split equally among all friends
5. The program asks if you want to use the "Who is lucky?" feature
6. If yes, it randomly selects one person who doesn't have to pay
7. The bill is recalculated, dividing the lucky person's share among the others
8. The final amount each person needs to pay is displayed

## Usage Example
```
Enter the number of friends joining (including you):
5
Enter the name of every friend (including you), each on a new line:
Marc
Jem
Monica
Anna
Jason
Enter the total bill value:
100
Do you want to use the "Who is lucky?" feature? Write Yes/No:
Yes
Jason is the lucky one!
{'Marc': 25.0, 'Jem': 25.0, 'Monica': 25.0, 'Anna': 25.0, 'Jason': 0}
```

## Skills Demonstrated
- Working with dictionaries in Python
- Random selection using the `random` module
- User input handling
- Conditional statements
- String formatting
- Basic arithmetic operations

## Requirements
- Python 3.6 or higher

You can install the required dependencies using:
```bash
pip install -r requirements_bill_splitter.txt
```