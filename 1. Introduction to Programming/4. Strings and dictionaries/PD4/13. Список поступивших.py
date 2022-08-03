students = {
    "Мария А.": 55,
    "Алексей А.": 78,
    "Иван Б.": 82,
    "Тоня И.": 79,
    "Дарья Ут.": 62,
    "Валерия К.": 69,
    "Дарья У.": 71,
}
sucsess_list = []
loser_list = []
user_input = int(input())
for student, score in students.items():
    if score>=user_input:
      sucsess_list.append(student)
    else:
     loser_list.append(student)

print("Поступили:")
[print(elem) for elem in sucsess_list]
print("Не поступили:")
[print(elem) for elem in loser_list]

