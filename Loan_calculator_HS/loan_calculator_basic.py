# %%
import math
principal_amount = float(input("Enter the loan principle:"))
mode = input('''What do you want to calculate?
type "m" - for number of monthly payments,
type "p" - for the monthly payment:''')

if mode == "m":
    monthly_payment = float(input("Enter the monthly payment:"))
    if principal_amount % monthly_payment == 0:
        print(f"It will take {int(principal_amount / monthly_payment)} months to repay the loan")
    else:
        print(f"It will take {math.ceil(principal_amount / monthly_payment)} months to repay the loan")

if mode == "p":
   no_of_months = int(input("Enter the number of months:"))
   if principal_amount % no_of_months == 0:
        monthly_payment = int(principal_amount / no_of_months)
        print(f"Your monthly payment = {monthly_payment}")
   else:
       monthly_payment = math.ceil(principal_amount / no_of_months)

       last_payment = int(principal_amount - (no_of_months-1) * monthly_payment)
       print(f"Your monthly payment = {monthly_payment} and the last payment = {last_payment}.")