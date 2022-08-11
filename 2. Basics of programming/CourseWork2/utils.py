"""
Module which load words and subwords, check correct of user subword

Functions:
    load_random_word() -> object

    check_word(player: object, word: object) -> None
"""

import random
from basic_word import BasicWord
import requests

URL = "https://jsonkeeper.com/b/ZQPG"


def load_random_word() -> object:
    """
    Load words and subwords from json
    Create object word from class BasicWord
    :return: object word from class BasicWord
    """

    # get data from json
    response = requests.get(URL)
    data = response.json()
    random_word = random.choice(data)

    # create object word from class BasicWord
    basic_word = BasicWord(random_word['word'], random_word['subwords'])
    return basic_word


def check_word(player: object, word: object) -> None:
    """
    Check correct of user subword
    :param player: object player from class Player
    :param word: object word from class BasicWord
    :return: None
    """
    while player.get_quantity_of_used_word() != word.word_count():
        user_word = input()
        if user_word == "stop":
            break
        elif len(user_word) < 3:
            print("слишком короткое слово")
        elif not word.is_subword(user_word):
            print("неверно")
        elif player.is_used(user_word):
            print("уже использовано")
        else:
            player.add_word(user_word)
            print("верно")
