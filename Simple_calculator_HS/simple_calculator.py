# %%
# The following script performs basic arithmetic operations and works like a simple calculator.

first_num = float(input('Enter first number: '))
second_num = float(input('Enter second number: '))
arithmetic_op = input('Enter arithmetic operation: ')

def simple_calculator(first_number, second_number, arithmetic_operation):
    try:
        if arithmetic_operation == '+':
            return first_number + second_number
        elif arithmetic_operation == '-':
            return first_number - second_number
        elif arithmetic_operation == '*':
            return first_number * second_number
        elif arithmetic_operation == '/':
            return first_number / second_number
        elif arithmetic_operation == 'mod':
            return first_number % second_number
        elif arithmetic_operation == 'pow':
            return first_number ** second_number
        elif arithmetic_operation == 'div':
            return first_number // second_number
    except ZeroDivisionError:
        return 'Division by 0!'

print(simple_calculator(first_num, second_num, arithmetic_op))

