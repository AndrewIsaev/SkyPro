class BasicWord:
    """
    Class with word and subwords

    Attributes
    ----------
    original_word : str
        original word
    list_of_subwords : list
        list of available subwords

    Methods
    -------
    is_subword()
        Check user word is subword or not
    word_count()
        Count amount of all available subwords from original word
    """

    def __init__(self, original_word: str, list_of_subwords: list):
        self.original_word = original_word
        self.list_of_subwords = list_of_subwords

    def __repr__(self):
        return f"Word: {self.original_word}\n" \
               f"Used words: {', '.join(self.list_of_subwords)}"

    def is_subword(self, word: str) -> bool:
        """
        Check user word is subword or not
        :param word: user word
        :return: True if user word is subword
                 False if user word isn`t subword
        """
        if word in self.list_of_subwords:
            return True
        return False

    def word_count(self) -> int:
        """
        Count amount of all available subwords from original word
        :return: amount of all available subwords
        """
        return len(self.list_of_subwords)
