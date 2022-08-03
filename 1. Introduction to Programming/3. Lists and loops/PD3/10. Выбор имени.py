serbian = ["Никола", "Лука", "Стефан", "Марко", "Лазар", "Александр", "Филип", "Йован", "Неманя", "Милош", "Душан"]
kazakh = ["Муртаза", "Меджит","Ильяс", "Харун", "Нурадил", "Айрат", "Азиль", "Ерлан"]
yakutian = ["Айхал", "Эркин", "Хорула", "Уруй", "Дуолан", "Дохсун", "Тимир"]

names_list = [serbian, kazakh, yakutian]
is_find = False

for name_list in names_list:

    for i in range(len(name_list)):
        print(f"Как вам имя {name_list[i]}?")
        yes_or_no = input("(да/нет)\n")

        if yes_or_no == "да":
            print("Отлично, вот мы и выбрали.")
            print("Я пойду :)")
            is_find = True
            break

    if is_find:
        break
    else:
        if name_list == serbian:
            print("Сербские имена закончились. Переходим к казахским!")
            continue
        elif name_list == kazakh:
            print("Казахские имена закончились. Переходим к якутским!")
            continue
        else:
            print("У меня закончились варианты, назовите его новый_сын_1")
            break




