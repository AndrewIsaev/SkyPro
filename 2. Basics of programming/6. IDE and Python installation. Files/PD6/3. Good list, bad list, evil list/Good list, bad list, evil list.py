import csv

with open("Students.csv", encoding="utf-8") as st:
    students_data = csv.reader(st)
    print(list(students_data))

with open("failed.txt", encoding="utf-8") as st:
    asd = st.read()

print(asd)
# for student in students_data:
#     if int(student[1]) >= 75:
#         with open("passed.txt", "a", encoding="utf-8") as passed:
#             passed.write(student[0]+"\n")
#     else:
#         with open("failed.txt", "a", encoding="utf-8") as failed:
#             failed.write(student[0]+"\n")
