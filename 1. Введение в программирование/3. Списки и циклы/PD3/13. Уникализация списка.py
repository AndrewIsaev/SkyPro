song_list = ["DRIVERS LICENSE", "DON'T PLAY", "AFTERGLOW", "SWEET MELODY", "AFTERGLOW", "STREETS",
             "AFTERGLOW", "YOU BROKE ME FIRST"]
sort_song_list = []
print("Список треков на сегодня:")
print()

for song in song_list:
    if song not in sort_song_list:
        sort_song_list.append(song)
        print(sort_song_list.index(song) + 1, song)
    else:
        print("X", song, "уже пели", sep=" ")
