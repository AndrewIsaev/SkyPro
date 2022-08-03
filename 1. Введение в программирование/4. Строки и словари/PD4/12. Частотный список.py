from pprint import pprint

marks = '''!()-[]{};?@#$%:'"\,./^&amp;*_«»'''
user_input = input()
for mark in marks:
    user_input = user_input.replace(mark, "")

words_list = list(user_input.lower().split())

dict_stat = {}
for word in set(words_list):
    counter = words_list.count(word)
    dict_stat[word] = counter

print(f"всего слов - {len(words_list)}")
pprint(dict_stat)
