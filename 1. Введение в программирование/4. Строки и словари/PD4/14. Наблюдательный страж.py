log_dict = {"Зашел": [], "Вышел": []}
income_list = []
outcome_list = []
while True:
    log = input("Запись\n")
    log_separate = list(log.split(": "))
    if log_separate[0] == "Зашел":
        income_list.append(log_separate[1])
        log_dict["Зашел"] = income_list
    elif log_separate[0] == "Вышел":
        outcome_list.append(log_separate[1])
        log_dict["Вышел"] = outcome_list
    else:
        break
not_outcome = []
only_outcome = []
income_and_outcome = []

for value in log_dict.values():
    for name in value:
        if log_dict["Зашел"].count(name) > log_dict["Вышел"].count(name):
            not_outcome.append(name)
        elif log_dict["Зашел"].count(name) < log_dict["Вышел"].count(name):
            only_outcome.append(name)
        else:
            income_and_outcome.append(name)

print(log_dict)
print("Зашли, но не вышли:")
[print(names) for names in set(not_outcome)]
print("Вышли, но не зашли:")
[print(names) for names in set(only_outcome)]
print("Зашли и вышли")
[print(names) for names in set(income_and_outcome)]
