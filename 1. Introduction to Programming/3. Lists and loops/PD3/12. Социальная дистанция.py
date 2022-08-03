counter = 0
scheme = input()
separate_scheme = scheme.split("_")
for item in separate_scheme:
    if len(item) > 1:
        counter += len(item)

print(f"Нарушителей замечено: {counter}")
