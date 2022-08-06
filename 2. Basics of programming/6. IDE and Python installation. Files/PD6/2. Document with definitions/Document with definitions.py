import csv
table = "table.csv"
with open(table, encoding="utf-8") as t:
    list_lines = list(csv.reader(t))
    print(list_lines)

dict_lines = {}
user_input = input("Ввод:\n").title()
for items in list_lines:
    dict_lines[items[0]] = items[1]

if user_input in dict_lines:
    print(f'{user_input} - {dict_lines[user_input]}')
else:
    print(f"По вашему запросу ничего не найдено, могу предложить:")
    [print(f"- {key}") for key in dict_lines.keys()]
