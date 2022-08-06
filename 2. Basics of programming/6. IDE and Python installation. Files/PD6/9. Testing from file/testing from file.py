import csv

with open("quiz.csv", encoding="utf-8") as file:
    quiz = list(csv.reader(file))

# print(quiz)
counter = 0
for question in quiz:
    print(f"Question {question[0]}. {question[1]}")
    print(f"[] {question[2]}")
    print(f"[] {question[3]}")
    user_answer = input("Ответ: ")
    if question[4] == user_answer:
        print("Верно")
        counter += 1
    else:
        print("Неверно")

print(f"Вы набрали {counter} баллов")