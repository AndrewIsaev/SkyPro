class Player:

    def __init__(self, username: str, user_used_words: list):
        self.username = username
        self.user_used_words = user_used_words

    def __repr__(self):
        return f"User: {self.username}\n" \
               f"Used words:{', '.join(self.user_used_words)}"


    def get_quantity_of_used_word(self):
        pass


    def add_word(self):
        pass


    def check_used_word(self):
        pass
