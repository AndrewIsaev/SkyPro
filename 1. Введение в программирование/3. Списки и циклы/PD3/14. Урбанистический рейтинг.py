# по количеству скамеечек на человека
top_by_benches = ["Auckland", "Osaka", "Adelaide", "Geneva", "Melbourne"]

# по количеству фонтанчиков на человека
top_by_fountains = ["Adelaide", "Geneva", "Osaka", "Melbourne", "Auckland"]

# по количеству качелек на человека
top_by_swings = ["Osaka", "Adelaide", "Geneva", "Melbourne", "Auckland"]

user_input = input()

print(f"по количеству скамеечек на человека: {top_by_benches.index(user_input)+1}")
print(f"по количеству фонтанчиков на человека: {top_by_fountains.index(user_input)+1}")
print(f"по количеству качелек на человека: {top_by_swings.index(user_input)+1}")

avg = (top_by_benches.index(user_input)+top_by_fountains.index(user_input)+top_by_swings.index(user_input)+3)/3
print(f"В среднем занимает позицию: {int(avg)}")