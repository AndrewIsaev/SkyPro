# user_number = int(input())
list_0_10 = ["ноль", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
list_20_90 = ["десять", "двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", "семьдесят", "восемьдесят",
              "девяносто"]
list_11_19 = ["одиннадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать", "шестнадцать", "семнадцать",
              "восемнадцать", "девятнадцать"]
first_part = ""
second_part = ""
for user_number in range(100):
    if 11 <= user_number <= 19:
        first_part = list_11_19[((user_number % 10) - 1)]
        second_part = ""
    elif user_number // 10 > 0 and user_number % 10 == 0:
        first_part = list_20_90[((user_number // 10) - 1)]
        second_part = ""
    elif user_number // 10 > 0:
        first_part = list_20_90[((user_number // 10) - 1)]
        second_part = list_0_10[user_number % 10]
    elif user_number % 10 in range(len(list_0_10)):
        first_part = list_0_10[user_number % 10]
        second_part = ""
    print(first_part + " " + second_part)
