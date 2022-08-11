from player import Player
from utils import load_random_word, check_word


def main():
    # player initialization
    print("Введите имя игрока")
    username = input()

    # create object player from class Player
    player = Player(username)
    # get object word from class BasicWord
    word = load_random_word()

    # Greeting and instructions
    print(f"Привет, {player.username}")
    print(f"Составьте {word.word_count()} слов из слова {word.original_word}")
    print(f"Слова должны быть не короче 3 букв")
    print(f"Чтобы закончить игру, угадайте все слова или напишите 'stop'")
    print(f"Поехали, ваше первое слово?")

    check_word(player, word)
    # output results
    print(f"Игра завершена, \
            вы угадали {player.get_quantity_of_used_word()} слов!")


if __name__ == "__main__":
    main()
