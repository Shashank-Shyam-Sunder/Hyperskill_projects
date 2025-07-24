# Simple Chatbot

## Overview
Simple Chatbot is an interactive Python program that simulates a conversation with a user. The chatbot introduces itself, asks for the user's name, guesses their age using a mathematical trick, demonstrates counting, tests the user's programming knowledge, and ends with a farewell message.

## Features
- Bot introduction with name and creation year
- User name recognition and greeting
- Age guessing using mathematical remainders
- Counting demonstration to any number
- Programming knowledge quiz with multiple-choice questions
- Structured conversation flow with different stages

## How It Works
The chatbot follows a structured conversation flow:

1. **Introduction**: The bot introduces itself with its name and creation year
2. **Name Recognition**: It asks for the user's name and responds with a greeting
3. **Age Guessing**: It guesses the user's age using remainders when dividing by 3, 5, and 7
4. **Counting Demonstration**: It counts from 0 to any number specified by the user
5. **Knowledge Test**: It tests the user's programming knowledge with a multiple-choice question
6. **Farewell**: It ends the conversation with a farewell message

## Age Guessing Algorithm
The chatbot uses a mathematical trick to guess the user's age:
1. It asks for the remainders when dividing the user's age by 3, 5, and 7
2. It calculates the age using the formula: `(rem3 * 70 + rem5 * 21 + rem7 * 15) % 105`
3. This formula works because of the Chinese Remainder Theorem in number theory

## Usage Example
```
Hello! My name is Bani.
I was created in 2023.
Please, remind me your name.
John
What a great name you have, John!
Let me guess your age.
Enter remainders of dividing your age by 3, 5 and 7.
1
2
3
Your age is 31; that's a good time to start programming!
Now I will prove to you that I can count to any number you want.
5
0 !
1 !
2 !
3 !
4 !
5 !
Let's test your programming knowledge.
Which of the following data types in Python is immutable?
1. Lists
2. Dictionaries
3. Tuples
4. Sets
3
Completed, have a nice day!
Congratulations, have a nice day!
```

## Skills Demonstrated
- Function definition and calling
- User input handling
- String concatenation and formatting
- Type conversion (string to int)
- Conditional statements
- Loops (while)
- Mathematical operations
- Structured program flow

## Requirements
- Python 3.6 or higher

## Customization
You can customize the chatbot by modifying:
- The bot's name and creation year in the `greet()` function call
- The quiz question and answers in the `test()` function
- The farewell message in the `end()` function