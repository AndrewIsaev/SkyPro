professions = {
"Мария А": "Фронтендер",
"Алексей А": "Фронтендер",
"Иван Б": "Бэкендер",
"Тоня И": "Бэкендер",
"Дарья У": "Тестировщик",
"Валерия К": "Бэкендер",
"Дарья У": "Тестировщик",
}
user_input = input()
for name, profession in professions.items():
    if user_input == profession:
        print(name, end=" ")