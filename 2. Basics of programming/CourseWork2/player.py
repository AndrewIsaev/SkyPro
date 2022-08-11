class Player:
    """
        Class with player and players word

        Attributes
        ----------
        username : str
            username
        ser_used_words : list
            list of right users subwords

        Methods
        -------
        get_quantity_of_used_word()
            Count used user words
        add_word()
            Add user subword in user subwords list
        is_used()
            Check was user word used or not
        """

    def __init__(self, username: str):
        self.username = username
        self.user_used_words = []

    def __repr__(self):
        return f"User: {self.username}\n" \
               f"Used words: {', '.join(self.user_used_words)}"

    def get_quantity_of_used_word(self) -> int:
        """
        Count used user words
        :return: Amount of used subwords
        """
        return len(self.user_used_words)

    def add_word(self, word: str) -> None:
        """
        Add user subword in user subwords list
        :param word: user word
        :return: None
        """
        self.user_used_words.append(word)

    def is_used(self, word: str) -> bool:
        """
        Check was user word used or not
        :param word: user word
        :return: True if used
                 False if not used
        """
        if word in self.user_used_words:
            return True
        return False
