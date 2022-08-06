with open("Nonsense.txt", encoding="utf-8") as file:
    text = file.read()
sentense_counter =0
words = text.count(" ") + 1
sentense_list = text.split(". ")
for sentense in sentense_list:
    if sentense[0].isupper():
        sentense_counter += 1

print(f"Предложений - {sentense_counter}")
print(f"Слов - {words}")
print(f"Символов – {len(text)}")