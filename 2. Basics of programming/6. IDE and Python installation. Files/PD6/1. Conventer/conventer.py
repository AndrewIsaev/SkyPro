miles = "miles.txt"
kilometers = "kilometers.txt"
with open(miles, encoding="utf-8") as file:
    miles_list = [float(line.strip()) for line in file]
with open(kilometers, "w", encoding="utf-8") as file:
    for miles in miles_list:
        km = miles * 1.609
        file.write(f"{km}\n")
