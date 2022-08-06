user_input = input()
counter = 0
with open("messages.txt", encoding="utf-8") as file:
    for line in file:
        if user_input.lower() in line.lower():
            counter += 1
print(f"Ищем: {user_input.lower()}")
print(f"Найдено сообщений {counter}")

