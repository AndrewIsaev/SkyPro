from pprint import pprint

user_word = ["офицер",
             "персей",
             "плюсна",
             "подруб",
             "подряд",
             "полиол",
             "популо",
             "свекла",
             "сизетт",
             "синьор",
             "усилие",
             "утенок"]

letters = [word[0] for word in user_word]
letter_dict = {letter: letters.count(letter) for letter in set(letters)}

for a, b in letter_dict.items():
    print(f"{a} - {b} слов")
