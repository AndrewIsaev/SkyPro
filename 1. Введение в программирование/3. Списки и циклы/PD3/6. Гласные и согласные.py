vowels = "AEIOUY"
consonants = "BCDFGHJKLMNPQRSTVWXYZ"
punctuation = """!()-[]{};:'"\, <>./#$%^&*_~'"""

user_input = input("Введите букву")
if user_input.isalpha():
    if user_input in vowels.upper():
        print("Это большая гласная")
    elif user_input in vowels.lower():
        print("Это маленькая гласная")
    elif user_input in consonants.upper():
        print("Это большая согласная")
    elif user_input in consonants.lower():
        print("Это маленькая согласная")
elif user_input.isdigit():
    print("Это цифра")
elif user_input in punctuation:
    print("Это знак препинания")
else:
    print("Это непонятно что")
