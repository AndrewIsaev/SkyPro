time = input()
hour = 0
minute = "00"
for symbol in time:
    if symbol == "*":
        hour += 1
    else:
        minute = int(minute)
        minute += 15

print(f'{hour}:{minute}')
