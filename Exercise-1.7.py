# mortgage.py

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1_000
months_elapsed = 1

while principal > 0:
    updated_payment = payment
    if months_elapsed >= extra_payment_start_month and months_elapsed <= extra_payment_end_month:
        updated_payment += extra_payment
    principal = principal * (1+rate/12) - updated_payment
    total_paid = total_paid + updated_payment
    print(months_elapsed, total_paid, principal)
    months_elapsed += 1

print('Total paid', total_paid)