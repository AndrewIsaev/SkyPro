import csv

with open("snakes.csv", encoding="utf-8") as file:
    result_table = list(csv.reader(file))

for snake in result_table:
    avg = (int(snake[1])+int(snake[2])+int(snake[3]))/3
    print(f"{snake[0]}: {avg: .2f}")
