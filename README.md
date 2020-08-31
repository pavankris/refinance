# Refinance - Outputs total interest paid for each row and also the monthly payments

## python refinance.py -i refinance_file.csv

**Refinance csv is self explanatory, just want to clarify two columns**
*loan_months* - How many months is this loan for
*loan_starting_month* - Which month the loan row is starting. The first row will be 0 and second row will be how many months have passed from first row as it's a refinance row.

**Output**
`('total_interest_paid: ', 527393.0127732742, ' in_months:', 345, ' with_monthly_payment', 4032.1967741793305)`

The total interest paid for the loan and how many months will the loan payout and what's the monthly payment.
You need to add with_monthly_payment and extra monthly from the row to see how much monthly is actually going from your bank.

**Ideal would be to make sure the loan term doesn't change from refinance, so adjust extra monthly in refinance row and calculate the gain because of refinance** 


