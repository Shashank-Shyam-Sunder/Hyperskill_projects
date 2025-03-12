import argparse
import math
parser = argparse.ArgumentParser(description='Loan Calculator which calculates one of the following parameters: '
                                             'Principal loan, Monthly annuity payment or number of months or payments')

parser.add_argument('--principal', type=float, nargs="?", help='Principal loan')
parser.add_argument('--payment', type=float, nargs="?", help='Amount of monthly payment')
parser.add_argument('--periods', type=int, nargs="?", help='Number of months')
parser.add_argument('--interest', type=float, nargs="?", help='Yearly interest rate')
parser.add_argument('--type', type=str, nargs="?", help='Type of payment: annuity or differentiated')
# parser.add_argument('--type', type=str, nargs="?", choices=["annuity", "diff"],
                    # help='Type of payment: annuity or differentiated')

args = parser.parse_args()
args_list = [args.principal, args.payment, args.periods, args.interest, args.type]
# Remove None values (for optional ingredients)
args_list = [ing for ing in args_list if ing is not None]
# print(args_list)

if not args.type:
    print("Incorrect parameters")
elif args.type != 'annuity' or args.type != 'differentiated':
    print("Incorrect parameters")

if args.type == "annuity":

    if not args.interest:
        print("Incorrect parameters")
    else:
        if not args.payment:
            int_rate = args.interest / 12 / 100
            monthly_payment = (args.principal * int_rate * (1 + int_rate) ** args.periods) / (
                        (1 + int_rate) ** args.periods - 1)
            monthly_payment = math.ceil(monthly_payment)
            print(f"Your monthly payment = {monthly_payment}!")
            overpayment = int(monthly_payment * args.periods) - args.principal
            print(f"Your overpayment = {int(overpayment)}")

        if not args.principal:
            int_rate = args.interest / 12 / 100
            principal_amount = (args.payment / (int_rate * (1 + int_rate) ** args.periods)) * (
                        (1 + int_rate) ** args.periods - 1)
            principal_amount = round(principal_amount)
            # principal_amount = principal_amount
            print(f"Your loan principle = {principal_amount}!")
            monthly_payment = args.payment
            overpayment = int(monthly_payment * args.periods) - principal_amount
            print(f"Your overpayment = {int(overpayment)}")

        if not args.periods:
            int_rate = args.interest / 12 / 100
            log_base = 1 + int_rate
            log_argument = (args.payment / (args.payment - int_rate * args.principal))
            no_months = math.log(log_argument, log_base)
            no_months = math.ceil(no_months)
            no_years = no_months // 12
            no_month = no_months % 12
            if no_month != 0:
                print(f"It will take {no_years} years and {no_month} months to repay this loan!")
            else:
                print(f"It will take {no_years} years to repay this loan!")
            monthly_payment = args.payment
            overpayment = int(monthly_payment * no_months) - args.principal
            print(f"Your overpayment = {int(overpayment)}")







if args.type == "diff":
    if args.principal and args.interest and args.periods:
        if (args.principal >=0) and (args.interest>=0)  and (args.periods>=0) :
            int_rate = args.interest / 12 / 100
            diff_monthly_payment = []
            for month in range(1,args.periods+1):
                diff_monthly_payment_temp = math.ceil((args.principal/args.periods) + int_rate * (args.principal - (args.principal*(month-1))/args.periods))
                diff_monthly_payment.append(diff_monthly_payment_temp)

            for month in range(1,args.periods+1):
                print(f"Month {month}: payment is {diff_monthly_payment[month-1]}")

            overpayment = int(sum(diff_monthly_payment) - args.principal)
            print(f"Overpayment: {overpayment}")

    else:
        print("Incorrect parameters")
