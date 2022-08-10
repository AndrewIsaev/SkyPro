import requests


class Questions:

    def __init__(self, question, difficult, right_answer, is_asked=False,
                 user_answer=None, score=0):
        self.question = question
        self.difficult = int(difficult)
        self.right_answer = right_answer

        self.is_asked = is_asked
        self.user_answer = user_answer
        self.score = int(score)

    def get_points(self):
        """Возвращает int, количество баллов.
        Баллы зависят от сложности: за 1 дается 10 баллов, за 5 дается 50 баллов.
        """
        self.score = self.difficult * 10
        return self.score

    def is_correct(self):
        """Возвращает True, если ответ пользователя совпадает
        с верным ответом иначе False.
        """
        return self.user_answer == self.right_answer

    def build_question(self):
        """Возвращает вопрос в понятном пользователю виде, например:
        Вопрос: What do people often call American flag?
        Сложность 4/5
        """
        return f"Вопрос: {self.question}\nСложность {self.difficult}/5"

    def build_positive_feedback(self):
        """Возвращает:
        Ответ верный, получено __ баллов
        """
        return f"Ответ верный, получено {self.score} баллов\n"

    def build_negative_feedback(self):
        """Возвращает:
        Ответ неверный, верный ответ __
        """
        return f"Ответ неверный, верный ответ {self.right_answer}\n"


def load_json(url: str) -> dict:
    """
    Load data from https://jsonkeeper.com/
    :param url: url with data
    :return: dict with data
    """
    response = requests.get(url)
    return response.json()


def get_questions(json_data: dict) -> list:
    """
    Get list with objects of class Questions
    :param json_data: list of dicts with fields question, difficult, right_answer
    :return: list of objects class Questions
    """
    questions = [Questions(*item.values()) for item in json_data]
    return questions


def get_sum_score(questions_list: list) -> tuple[int, int]:
    """
    Get statistics from object in list
    :param questions_list: List
    :return: tuple(summ, questions amount)
    """
    summ = 0
    for question in questions_list:
        summ += question.score
    return summ, len(questions_list)


def print_statistics(rigth_answer_counter: int, summ: int,
                     questions_amount: int) -> None:
    """
    Print statistics
    :param rigth_answer_counter: quantity of right answers
    :param summ: total score
    :param questions_amount: quantity of questions
    :return: Example:
    Вот и всё!
    Отвечено 0 вопроса из 5
    Набрано баллов: 0
    """
    print("Вот и всё!")
    print(f"Отвечено {rigth_answer_counter} вопроса из {questions_amount}")
    print(f"Набрано баллов: {summ}")
