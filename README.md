# Hyperskill Python Projects

This repository contains Python projects completed as part of the [Hyperskill](https://hyperskill.org/) learning platform. These projects cover fundamental and advanced programming concepts, demonstrating various aspects of Python programming.

## 📂 Projects Overview

| Project | Description |
|---------|-------------|
| [Account Management](#account-management) | A simple shop accounting system to track income and expenses |
| [Bill Splitter](#bill-splitter) | A tool to split bills among friends with a "lucky person" feature |
| [File Manager](#file-manager) | A command-line file system navigator and manager |
| [HTTP Requests](#http-requests) | Examples of using Python's requests library for API interactions |
| [Loan Calculator](#loan-calculator) | A tool to calculate loan parameters with different payment types |
| [Regular Expressions](#regular-expressions) | Examples and exercises for using regular expressions in Python |
| [Simple Calculator](#simple-calculator) | A basic calculator supporting various arithmetic operations |
| [Simple Chatbot](#simple-chatbot) | An interactive chatbot with various conversation features |
| [Zookeeper](#zookeeper) | A virtual zoo simulation with ASCII art animals |

## 🔍 Project Details

### Account Management
A simple shop accounting system that tracks item prices, calculates total income, and determines net income after expenses.

**Features:**
- Store and display shop items with their prices
- Track earnings for each item
- Calculate total and net income
- Handle user input for expenses

### Bill Splitter
A bill splitting application that divides a bill among friends, with an option to randomly select one person who doesn't have to pay.

**Features:**
- Input number of friends and their names
- Split bill equally among all friends
- "Who is lucky?" feature to exempt one person from payment
- Recalculate shares when a lucky person is selected

### File Manager
A command-line file system navigator that allows users to explore directories and files.

**Features:**
- Navigate directories with cd commands
- View current directory with pwd
- List directory contents with ls
- View file sizes in different formats (bytes, KB, MB, GB)
- Error handling for invalid commands and paths

### HTTP Requests
Examples of using Python's requests library for HTTP operations and API interactions.

**Features:**
- Make GET requests to various websites and APIs
- Handle response status codes and content
- Parse JSON responses
- Implement caching for API requests
- Weather data API integration with TTL caching

### Loan Calculator
A loan calculator that computes different loan parameters based on user input.

**Features:**
- Calculate monthly payment, loan principal, or number of payments
- Support for annuity and differentiated payment types
- Interest rate calculations
- Command-line argument parsing
- Overpayment calculation

### Regular Expressions
A collection of examples and exercises demonstrating the use of regular expressions in Python.

**Features:**
- Pattern matching with re.match(), re.search(), re.findall()
- Text substitution with re.sub()
- String splitting with re.split()
- Various regex patterns and concepts
- Regex flags for case-insensitive and multi-line matching

### Simple Calculator
A basic calculator that performs arithmetic operations on two numbers.

**Features:**
- Addition, subtraction, multiplication, division
- Modulus, power, and integer division operations
- Error handling for division by zero

### Simple Chatbot
An interactive chatbot that engages users in conversation and demonstrates various programming concepts.

**Features:**
- Introduction and name recognition
- Age guessing using mathematical tricks
- Counting demonstration
- Programming knowledge quiz
- Structured conversation flow

### Zookeeper
A virtual zoo simulation that displays ASCII art representations of animals based on user input.

**Features:**
- ASCII art representations of various animals
- Interactive habitat selection
- Loop-based interaction until exit command

## 🚀 Usage
Clone this repository and navigate to a project folder:
```bash
git clone https://github.com/Shashank-Shyam-Sunder/Hyperskill_projects.git
cd Hyperskill_projects
```

To run a specific project, navigate to its directory and execute the Python file:
```bash
cd Zookeeper_with_python_HS
python zookeeper_with_python.py
```

## 📚 Learning Path
These projects represent a progression in Python programming skills, from basic concepts to more advanced topics:

1. **Beginner**: Zookeeper, Simple Calculator, Simple Chatbot
2. **Intermediate**: Bill Splitter, Account Management, Loan Calculator
3. **Advanced**: File Manager, Regular Expressions, HTTP Requests

Each project focuses on different aspects of Python programming and builds upon previously learned concepts.

## 📝 Requirements
The projects require Python 3.6 or higher. Some projects may require additional libraries, which can be installed using:
```bash
pip install -r requirements.txt
```
