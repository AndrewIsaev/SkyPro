# Объявляем исходные словари
words_easy = {
    "family": "семья",
    "hand": "рука",
    "people": "люди",
    "evening": "вечер",
    "minute": "минута",
}

words_medium = {
    "believe": "верить",
    "feel": "чувствовать",
    "make": "делать",
    "open": "открывать",
    "think": "думать",
}

words_hard = {
    "rural": "деревенский",
    "fortune": "удача",
    "exercise": "упражнение",
    "suggest": "предлагать",
    "except": "кроме",
}

levels = {
    0: "Нулевой",
    1: "Так себе",
    2: "Можно лучше",
    3: "Норм",
    4: "Хорошо",
    5: "Отлично",
}

# Создаем словарь ответов
answers = {}

# Создаем необходимые переменные
right_answers_count = 0
correct_answers_list = []
incorrect_answers_list = []

# Выводим запрос уровня сложности и получаем ответ
print("Выберите уровень сложности.")
print("Легкий, средний, сложный.")
user_difficult_level = input()


# Выбираем сложность в зависимости от ввода пользователя
if user_difficult_level.lower() == "легкий":
    words = words_easy
elif user_difficult_level.lower() == "средний":
    words = words_medium
elif user_difficult_level.lower() == "сложный":
    words = words_hard
else:
    quit("Такого уровня не существует")

print(f"Выбран уровень сложности - {user_difficult_level.title()}, мы предложим 5 слов, подберите перевод.")

while True:
    # Перебираем словарь по ключу и значению
    for word_en, word_ru in words.items():
        # Предлагаем нажать Enter для старта
        print("Нажмите Enter.")
        user_input_ENTER = input()

        # Задаем вопрос и получаем ответ
        print(f"{word_en}, {len(words[word_en])} букв, начинается на {words[word_en][0]}")
        user_answer = input()

        # Проверяем правильный ответ или нет и заполняем словарь с правильными/неправильными ответами
        if user_answer == words[word_en]:
            print(f"Верно, {word_en.title()} - это {words[word_en]}")

            answers[word_en] = True
        else:
            print(f"Неверно. {word_en.title()} -  это {words[word_en]}.")

            answers[word_en] = False
    # Создаем список правильных и неправильных ответов
    for answer, is_correct in answers.items():
        if is_correct:
            correct_answers_list.append(answer)
            right_answers_count += 1
        else:
            incorrect_answers_list.append(answer)
    # Выводим результат
    print("Правильно отвечены слова:")
    [print(item) for item in correct_answers_list]

    print("Неправильно отвечены слова:")
    [print(item) for item in incorrect_answers_list]

    print("Ваш ранг:", levels[right_answers_count], sep="\n")
    break
