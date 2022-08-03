def check_brackets(user_string):
    if user_string.count("(") == user_string.count(")"):
        if user_string.find("(") <= user_string.find(")"):
            return True
    return False


print(check_brackets("(a+b)"))
print(check_brackets("a+b"))
print(check_brackets("(a+b) * c"))

print(check_brackets("(a+b"))
print(check_brackets(")a+b)"))
print(check_brackets(")a+b("))
print(check_brackets("(a+b * c"))
