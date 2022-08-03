def check_phone_number(number: str):
    for symbol in "+-()":
        number = number.replace(symbol, "")
    if number.isdigit():
        return True
    return False


print(check_phone_number("+7(930)8167853"))
print(check_phone_number("+7(930)81678f3"))
