class BasicWord:

    def __init__(self, original_word: str, list_of_subwords: list):
        self.original_word = original_word
        self.list_of_subwords = list_of_subwords


    def __repr__(self):
        return f"Word: {self.original_word}\n" \
               f"Used words:{', '.join(self.list_of_subwords)}"

    def check_subword(self):
        pass


    def word_count(self):
        pass


