monthly_payment = 0
bank_percent = 0.01
sum = 0
month_count = 0

while sum <= 15000:
    monthly_payment += 1000
    sum = monthly_payment + monthly_payment * bank_percent
    month_count += 1

print(month_count)