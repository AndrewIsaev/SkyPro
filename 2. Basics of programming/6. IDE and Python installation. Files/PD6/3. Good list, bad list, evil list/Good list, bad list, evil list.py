import csv

with open("Students.csv", encoding="utf-8") as st:
    students_data = list(csv.reader(st))

print(students_data)
for student in students_data:
    if int(student[1]) >= 75:
        with open("passed.txt", "a", encoding="utf-8") as passed:
            passed.write(student[0]+"\n")
    else:
        with open("failed.txt", "a", encoding="utf-8") as failed:
            failed.write(student[0]+"\n")
