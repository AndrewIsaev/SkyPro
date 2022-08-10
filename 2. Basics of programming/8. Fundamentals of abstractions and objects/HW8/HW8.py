from utils import get_sum_score, get_questions, load_json, print_statistics
import random

URL = "https://jsonkeeper.com/b/EZEO"

json_data = load_json(URL)
questions = get_questions(json_data)

rigth_answer_counter = 0
random.shuffle(questions)

for question in questions:
    if question.is_asked == False:
        print(question.build_question())
        question.is_asked = True
        question.user_answer = input("Answer: ")

        if  question.is_correct():
            question.get_points()
            print(question.build_positive_feedback())
            rigth_answer_counter += 1
        else:
            print(question.build_negative_feedback())

print_statistics(rigth_answer_counter, *get_sum_score(questions))