# Приветствие
print('Привет!')
print('Предлагаю проверить свои знания английского!')

# Запрос имя пользователя
student_name = input('Расскажи, как тебя зовут!\n')
print(f'Привет, {student_name}, начинаем тренировку!')

# Обьявляем счетчик правильныз ответов  и количество баллов
right_answers = 0
score = 0

# задаем 1 вопрос и получаем ответ
first_answer = input('My name ___ Vova\n')

# проверяем корректный ли ответ
if first_answer == 'is':
    # увеличиваем количество правильных ответов на 1 баллы на 10
    right_answers += 1
    score += 10

    # выводим результаты
    print('Ответ верный!')
    print('Вы получаете 10 баллов!')
else:
    print('Неправильно.')
    print('Правильный ответ: is')

# задаем 2 вопрос и получаем ответ
second_answer = input('I ___ a coder\n')

# проверяем корректный ли ответ
if second_answer == 'am':
    # увеличиваем количество правильных ответов на 1 баллы на 10
    right_answers += 1
    score += 10

    # выводим результаты
    print('Ответ верный!')
    print('Вы получаете 10 баллов!')
else:
    print('Неправильно.')
    print('Правильный ответ: am')

# # задаем 3 вопрос и получаем ответ
third_answer = input('I live ___ Moscow\n')

# проверяем корректный ли ответ
if third_answer == 'in':
    # увеличиваем количество правильных ответов на 1 баллы на 10
    right_answers += 1
    score += 10

    # выводим результаты
    print('Ответ верный!')
    print('Вы получаете 10 баллов!')
else:
    print('Неправильно.')
    print('Правильный ответ: in')

# считаем проценты правильных ответов
right_answers_percent = round(right_answers / 3 * 100)

# выводим общий результат
print(f'Вот и все, {student_name}!')
print(f'Вы ответили на {right_answers} вопросов из 3 верно.\n')
print(f'Вы заработали {score} баллов.')
print(f'Это {right_answers_percent} процентов.')

