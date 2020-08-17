
import argparse
import csv
#import numpy
import math

def calculate_monthly(loan_amount, interest, loan_months):
    #monthly = numpy.pmt(interest/12/100, loan_months, -loan_amount)
    r = interest/100
    i = r / 12
    monthly = (loan_amount * i) / (1 - math.pow(1 + i, -loan_months))
    return monthly

def calculate_interest(balance, interest):
    return balance * (interest/12/100)

def should_refinance(refin_file):
    loan_payments = []
    with open(refin_file) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            loan_payments_row = []
            loan_amount = float(row['loan_amount'])
            interest = float(row['interest'].replace('%', ''))
            loan_months = int(row['loan_months'])
            extra_monthly = float(row['extra_monthly'])
            loan_starting_month = int(row['loan_starting_month'])
            monthly_payment = calculate_monthly(loan_amount, interest, loan_months)
            print(monthly_payment)
            loan_balance = loan_amount
            if loan_starting_month > 0 and len(loan_payments) > 0:
                wasted_interest_payments = 0
                for i in range(loan_starting_month):
                    wasted_interest_payments += loan_payments[0][i]['interest_payment']
                loan_payments_row.append({
                    'month': 0,
                    'starting_balance': loan_balance,
                    'interest_payment': wasted_interest_payments,
                    'principle_payment': 0.0,
                    'ending_balance': ending_balance
                })
            for i in range(loan_months):
                interest_payment = calculate_interest(loan_balance, interest)
                principle_payment = monthly_payment - interest_payment
                ending_balance = loan_balance - principle_payment - extra_monthly
                loan_payments_row.append({
                    'month': i,
                    'starting_balance': loan_balance,
                    'interest_payment': interest_payment,
                    'principle_payment': principle_payment,
                    'ending_balance': ending_balance
                })
                loan_balance = ending_balance
                if ending_balance <= 0:
                    break
            loan_payments.append(loan_payments_row)
    for payments in loan_payments:
        total_interest_paid = 0.0
        for monthly_payments in payments:
            total_interest_paid += monthly_payments['interest_payment']
        print('total_interest_paid: ', total_interest_paid)


def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('-i', '--refin_file', metavar='in_file')
  parsed = parser.parse_args()
  should_refinance(parsed.refin_file)

if __name__ == "__main__":
  main()