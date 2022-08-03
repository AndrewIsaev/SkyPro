from pprint import pprint

song_list = ["Galibri & Mavik – Федерико Феллини", "DaBro - На Часах Ноль-Ноль",
             "Dead Blonde – Мальчик На Девятке",
             "Султан Лагучев - Горький Вкус",
             "Султан Лагучев - Горький Вкус",
             "Султан Лагучев - Горький Вкус",
             "NK – Красное Вино",
             "Dead Blonde - Бесприданница",
             "Клава Кока & Руки Вверх - Нокаут",
             "Minelli - Rampampam",
             "Хабиб feat. DJ Smash - Беги",
             "Асия & Аня Pokrov - Любовь С Картинки",
             "Артём Пивоваров - Рандеву",
             "Хабиб - Грустинка",
             "Konfuz - Ратата",
             "Amri - Звезда Тик-Ток",
             "Ваня Дмитриенко - Венера-Юпитер",
             "Galibri & Mavik - Федерико Феллини (Pitched Version)",
             "NLO - Не Грусти"]
song_dict = {}
for song in set(song_list):
    song_dict[song] = song_list.count(song)

pprint(song_dict)
