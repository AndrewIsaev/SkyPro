user_email = input()
free_domain = ["yandex.ru", "mail.ru", "gmail.com", "yahoo.com", "rambler.ru"]

user_domain = user_email.split("@")[1]

if "@" not in user_email or "." not in user_domain:
    print("Это вообще не почта")
elif user_domain in free_domain:
    print("Это почта, она на бесплатном домене")
else:
    print("Это почта, она на корпоративном домене")

