import math
import sys
arguments = sys.argv

def data_input():
    loan_type = ''
    principal = 0
    payment = 0
    periods = 0
    interest = 0
    for element in arguments:  # retrieves different parameters from the command line
        if '--type=' in element:
            loan_type += element.replace('--type=', '')
        elif '--principal=' in element:
            principal += int(element.replace('--principal=', ''))
        elif '--payment=' in element:
            payment += int(element.replace('--payment=', ''))
        elif '--periods=' in element:
            periods += int(element.replace('--periods=', ''))
        elif '--interest=' in element:
            interest += float(element.replace('--interest=', ''))
    if len(arguments) >= 5 and (type == 'annuity' or type == 'diff'):  # checks parameters' correctness, enters the right module
        if principal == 0 and type == 'annuity' and payment > 0 and periods > 0 and interest > 0:
            calculate_loan_principal(payment, periods, interest)
        elif payment == 0 and principal > 0 and periods > 0 and interest > 0:
            calculate_monthly_payment(type, principal, periods, interest)
        elif periods == 0 and type == 'annuity' and principal > 0 and payment > 0 and interest > 0:
            calculate_payments_number(principal, payment, interest)
        else:
            print('Incorrect parameters')
    else:
        print('Incorrect parameters')

def calculate_payments_number(principal, payment, interest):  # calculates number of payments
    nominal_interest = interest / (12 * 100)
    periods = math.ceil(math.log(payment / (payment - (nominal_interest * principal)), 1 + nominal_interest))
    if periods < 12:
        print(f'It will take {periods} months to repay the loan')
    elif periods == 12:
        print(f'It will take 1 year to repay the loan')
    elif 12 < periods < 24:
        print(f'It will take 1 year and {periods % 12} months to repay the loan')
    else:
        if periods % 12 == 0:
            print(f'It will take {int(periods / 12)} years to repay the loan')
        else:
            print(f'It will take {periods // 12} years and {periods % 12}to repay the loan')
    print(f'Overpayment = {int(payment * periods - principal)}')

def calculate_monthly_payment(loan_type, principal, periods, interest):  # calculates monthly payment
    nominal_interest = interest / (12 * 100)
    if loan_type == 'annuity':  # monthly annuity payment
        annuity_payment = math.ceil(principal * (nominal_interest * math.pow(1 + nominal_interest, periods)) / ((pow(1 + nominal_interest, periods)) - 1))
        print(f'Your monthly payment = {annuity_payment}!')
        print(f'Overpayment = {annuity_payment * periods - principal}')
    elif loan_type == 'diff':  # monthly differentiate payment
        diff_payment_sum = 0.0
        for i in range(1, periods + 1):
            diff_payment = (principal / periods) + (nominal_interest * (principal - ((principal * (i - 1)) / periods)))
            print(f'Month {i}: payment is {math.ceil(diff_payment)}')
            diff_payment_sum += math.ceil(diff_payment)
        print(f'\nOverpayment = {int(diff_payment_sum - principal)}')

def calculate_loan_principal(payment, periods, interest):  # calculates loan principal
    nominal_interest = interest / (12 * 100)
    principal = payment / ((nominal_interest * math.pow(1 + nominal_interest, periods)) / ((pow(1 + nominal_interest, periods)) - 1))
    print(f'Your loan principal = {int(principal)}!')
    print(f'Overpayment = {math.ceil(payment * periods - principal)}')

data_input()