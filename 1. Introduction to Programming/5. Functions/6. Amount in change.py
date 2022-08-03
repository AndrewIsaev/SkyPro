def change(sum_rub, money_list):
    money_dict = {}
    for money in money_list:
        money_count = sum_rub // money
        sum_rub -= money * money_count
        money_dict[money] = money_count

    return money_dict


print(change(27, [10, 5, 2, 1]))
print(change(19, [10, 2, 1]))
print(change(94, [10, 1]))
