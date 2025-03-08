# %% Listing all items available for sale with their prices in a dictionary
shop_items = {"Bubblegum": 2, "Toffee": 0.2, "Ice cream": 5,
              "Milk chocolate": 4, "Doughnut": 2.5, "Pancake": 3.2}

# Displaying the prices of items itemwise
print("Prices:")
for key, value in shop_items.items():
    print(f"{key}: ${value}")

# %% Measuring total income of your shop
shop_items_earnings = {"Bubblegum": 202, "Toffee": 118, "Ice cream": 2250,
              "Milk chocolate": 1680, "Doughnut": 1075, "Pancake": 80}

print("Earned amount:")
total_income = 0

for key, value in shop_items_earnings.items():
    print(f"{key}: ${value}")
    total_income += value

print(f"\nIncome: ${total_income}" )

# Asking for staff and other expenses from the user which is owner in the present case
staff_expenses = input("Staff expenses: ")
other_expenses = input("Other expenses: ")

# Computing the net income of the shop and printing it
net_income = total_income - int(staff_expenses) - int(other_expenses)
print(f"Net income: ${net_income}")