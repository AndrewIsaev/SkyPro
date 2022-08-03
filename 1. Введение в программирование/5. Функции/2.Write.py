def return_words_between_start_and_stop(user_str: str):
    user_str_list = user_str.split()
    return " ".join(user_str_list[
                    user_str_list.index("старт") + 1:user_str_list.index(
                        "стоп")])


a = "начнем готовы старт добро пожаловать стоп снято вот и закончим"
print(return_words_between_start_and_stop(a))
