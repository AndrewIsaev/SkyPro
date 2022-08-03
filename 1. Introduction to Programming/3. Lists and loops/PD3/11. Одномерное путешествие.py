game_map = ["трава", "камни", "озеро", "озеро", "песок", "камни", "земля"]
i = 0
while True:
    print(f"Вы находитесь на клетке {i + 1}.Вокруг вас {game_map[i]}")
    print("Куда вы пойдете: вперед или назад?")
    user_choice = input()
    if user_choice == "вперед" and i < len(game_map)-1:
        i += 1
    else:
        if i < 1 or i >= len(game_map)-1:
            print("Там ничего нет, туда идти нельзя.")
        else:
            i -= 1
