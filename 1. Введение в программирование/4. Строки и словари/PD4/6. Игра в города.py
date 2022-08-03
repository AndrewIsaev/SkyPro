cities = input()
cities_list = list(cities.split(" - "))

is_correct = False

for i in range(len(cities_list) - 1):
    if cities_list.count(cities_list[i]) > 2:
        print("Правила нарушены")
        break
    elif cities_list[i].lower()[-1] == "ь" or cities_list[i+1].lower()[-1] == "ы":
        if cities_list[i].lower()[-2] != cities_list[i+1].lower()[0]:
            print("Правила нарушены")
            break
    elif cities_list[i].lower()[-1] != cities_list[i+1].lower()[0]:
            print("Правила нарушены")
            break
    else:
        is_correct = True

if is_correct:
    print("Правила не нарушены")

