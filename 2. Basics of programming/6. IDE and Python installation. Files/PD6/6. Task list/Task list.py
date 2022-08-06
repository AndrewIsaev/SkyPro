from pprint import pprint

todo_dict = {}
counter = 0
with open("todo.txt", encoding="utf-8") as file:
    for line in file:
        task, status = line.split(": ")
        todo_dict[task] = status.strip()
        if status.strip() == "DONE":
            counter += 1

print(f"В списке {len(todo_dict)} дел")
print(f"Сделано {counter}/{len(todo_dict)}")
print(f"Давай пройдемся по твоим делам!")

for key, value in todo_dict.items():
    if value == "TODO":
        print(f"{key} - сделано? (y/n)")
        user_input = input()
        if user_input == "y":
            todo_dict[key] = "DONE"

with open("todo.txt", "w", encoding="utf-8") as file:
    for key, value in todo_dict.items():
        file.write(f"{key}: {value}\n")



