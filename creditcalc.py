import math
import argparse

parser = argparse.ArgumentParser(exit_on_error=False)

parser.add_argument("--type")
parser.add_argument("--principal")
parser.add_argument("--periods")
parser.add_argument("--interest")
parser.add_argument("--payment")

try:
    args = parser.parse_args()
    type = args.type

    loan_interest = float(args.interest)
    if loan_interest < 0:
        raise Exception

except:
    print("Incorrect parameters.")
    exit(0)

try:
    loan_principal = int(args.principal)
    if loan_principal < 0:
        print("Incorrect parameters.")
        exit(0)
except:
    loan_principal = None

try:
    num_of_periods = int(args.periods)
    if num_of_periods < 0:
        print("Incorrect parameters.")
        exit(0)
except:
    num_of_periods = None

try:
    monthly_payment = int(args.payment)
    if monthly_payment < 0:
        print("Incorrect parameters.")
        exit(0)
except:
    monthly_payment = None

i = loan_interest / (12 * 100)

if type == "diff":
    sum_of_payment = 0
    for num_of_month in range(1, num_of_periods + 1):
        payment = math.ceil(loan_principal / num_of_periods + i * (loan_principal - (loan_principal * (num_of_month - 1) / num_of_periods)))
        print(f"Month {num_of_month}: payment is {payment}")
        sum_of_payment += payment
    print(f"\nOverpayment = {sum_of_payment - loan_principal}")
elif type == "annuity":
    if loan_principal != None and num_of_periods != None:
        monthly_payment = math.ceil(loan_principal * (i * (1 + i) ** num_of_periods) / ((1 + i) ** num_of_periods - 1))
        print(f"Your monthly payment = {monthly_payment}!")
        print(f"Overpayment = {monthly_payment * num_of_periods - loan_principal}")
    elif monthly_payment != None and num_of_periods != None:
        loan_principal = math.floor(monthly_payment / ((i * (1 + i) ** num_of_periods) / ((1 + i) ** num_of_periods - 1)))
        print(f"Your loan principal = {loan_principal}!")
        sum_of_payment = num_of_periods * monthly_payment
        print(f"Overpayment = {sum_of_payment - loan_principal}")
    elif loan_principal != None and monthly_payment != None:
        num_of_month = math.ceil(math.log(monthly_payment / (monthly_payment - i * loan_principal), 1 + i))
        num_of_years = num_of_month // 12
        num_of_month_only = num_of_month % 12
        if num_of_years == 1:
            num_of_years_noun = "year"
        else:
            num_of_years_noun = "years"
        if num_of_month_only == 1:
            num_of_month_noun = "month"
        else:
            num_of_month_noun = "months"

        if num_of_month_only > 0 and num_of_years > 0:
            print(
                f"It will take {num_of_years} {num_of_years_noun} and {num_of_month_only} {num_of_month_noun} to repay this loan")
        elif num_of_month_only > 0:
            print(f"It will take {num_of_month_only} {num_of_month_noun} to repay this loan")
        else:
            print(f"It will take {num_of_years} {num_of_years_noun} to repay this loan")

        sum_of_payment = num_of_month * monthly_payment
        print(f"Overpayment = {sum_of_payment - loan_principal}")