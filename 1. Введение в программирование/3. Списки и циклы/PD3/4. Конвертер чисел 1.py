numbers_names = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
numbers_names_more_twenty = ["twen", "thir", "for", "fif", "six", "seven", "eigh", "nine"]
eleven_twelve_list = ["eleven", "twelve"]


first_part = ""
second_part = ""

user_number = input()
user_number_list = user_number.split(" ")

if len(user_number_list) != 1:
    if user_number_list[0][0:-2] in numbers_names_more_twenty:
        first_part = str(numbers_names_more_twenty.index(user_number_list[0][0:-2]) + 2)
        second_part = str(numbers_names.index(user_number_list[1]))
else:
    if user_number_list[0][0:-2] in numbers_names_more_twenty:
        first_part = str(numbers_names_more_twenty.index(user_number_list[0][0:-2]) + 2)
        second_part = "0"

    elif user_number_list[0][0:-4] in numbers_names_more_twenty:
        first_part = "1"
        second_part = str(numbers_names_more_twenty.index(user_number_list[0][0:-4]) + 2)

    elif user_number_list[0] in eleven_twelve_list:
        first_part = "1"
        second_part = str(eleven_twelve_list.index(user_number_list[0]) + 1)

    elif user_number_list[0] in numbers_names:
        first_part = str(numbers_names.index(user_number_list[0]))

print(first_part + second_part)
