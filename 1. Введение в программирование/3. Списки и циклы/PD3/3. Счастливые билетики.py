user_ticket_number = input("Введите номер билетика")
ticket_number_list =[]
if len(user_ticket_number) != 6:
    print("Не хватает цифр на билетике, возможно, вы уже съели часть?")
else:
    ticket_number_list = list(user_ticket_number)
    first_part_sum = int(ticket_number_list[0])+int(ticket_number_list[1])+int(ticket_number_list[2])
    second_part_sum = int(ticket_number_list[3]) + int(ticket_number_list[4]) + int(ticket_number_list[5])
    if first_part_sum == second_part_sum:
        print("Это счастливый билетик, ешьте его скорей!")
    else:
        print("Это обычный билетик, но вы все равно можете его съесть!")