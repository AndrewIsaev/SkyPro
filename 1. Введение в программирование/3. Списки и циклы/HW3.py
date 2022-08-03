# обьявляем переменные
questions = ["My name ___ Vova", "I ___ a coder", "I live ___ Moscow"]
answers = ["is", "am", "in"]
right_answers = 0
score = 0

# Вывод приветствия и условий для начала игры
print('Привет! Предлагаю проверить свои знания английского! Наберите "ready", чтобы начать!')
is_ready = input()

# Проверка условия на запуск игры
if is_ready == 'ready':
    # Создадим цикл, который будет перебирать индексы вопросов и ответов
    for i in range(len(questions)):
        # Создадим цикл, который будет перебирать попытки
        attempt = 3
        while attempt > 0:
            # задаем вопрос и получаем ответ
            print(questions[i])
            user_answer = input()
            # проверяем корректный ли ответ
            if user_answer == answers[i]:
                print('Ответ верный!')
                # увеличиваем количество правильных ответов на 1 баллы на число попыток + 1
                right_answers += 1
                score += attempt
                # Выходим из цикла и переходим к следующему вопросу
                break
            else:
                # Если попытки кончились
                attempt -= 1
                if attempt == 0:
                    print(f'Увы, но нет. Верный ответ: {answers[i]}')
                else:
                    # Выводим оставшиеся попытки
                    print(f'Осталось попыток: {attempt}, попробуйте еще раз!')

    # выводим общий результат
    print(f'Вот и все! Вы ответили на {right_answers} вопросов из {len(questions)} верно, вы набрали {score} баллов.')
else:
    # Если пользователь ввел не ready
    print('Кажется, вы не хотите играть. Очень жаль.')
