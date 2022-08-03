from pprint import pprint


def validate(candidate):
    if 157 <= candidate["h"] <= 175 and 50 <= candidate["w"] <= 70:
        return True


def validate_list(candidates_list):
    good_candidate = []
    for candidate in candidates_list:
        if validate(candidate):
            good_candidate.append(candidate)
    return good_candidate


candidates = [
    {"name": "Юрий", "h": 157, "w": 60},
    {"name": "Олег", "h": 177, "w": 65},
    {"name": "Юлия", "h": 165, "w": 57},
    {"name": "Аркадий", "h": 174, "w": 59},
]

# #assert validate({"h": 160, "w": 60})  # "Ошибка для роста 160 и веса 60"
# assert validate({"h": 180, "w": 60}) == False # "Ошибка для роста 160 и веса 60"
# assert validate({"h": 164, "w": 75})  # "Ошибка для роста 160 и веса 60"
# assert validate({"h": 180, "w": 80})  # "Ошибка для роста 160 и веса 60"

assert validate_list(candidates) == [candidates[0], candidates[2],
                                     candidates[3]]

pprint(validate_list(candidates), sort_dicts=False)
