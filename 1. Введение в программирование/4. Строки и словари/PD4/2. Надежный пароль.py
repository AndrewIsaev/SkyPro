login = input()
password = input()
counter_login = 0
is_digit_in_password = False

for symbol in password:
    if symbol.isdigit():
        is_digit_in_password = True

if len(login) > 3 and len(password) > 8 and is_digit_in_password:
    print("Это хорошие логин и пароль!")
else:
    if len(login) < 3:
        print("Логин должен содержать больше 3 символов.")
    if len(password) < 8:
        print("Пароль должен содержать больше 8 символов.")
    if not is_digit_in_password:
        print("Пароль должен содержать хотя бы одну цифру.")

