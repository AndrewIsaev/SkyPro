import csv

with open("expenses.csv", encoding="utf-8") as file:
    expenses_list = list(csv.reader(file))
summ = 0
for expense in expenses_list:
    summ += int(expense[1])

print(f"Всего позиций: {len(expenses_list)}")
print(f"Сумма: {summ}")