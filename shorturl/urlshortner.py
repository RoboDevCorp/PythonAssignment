import random
import string

#default_token_size = 5

class urlshortner:
    token_size = 6

    def __init__(self, token_size=None):
        self.token_size = token_size if token_size is not None else 5

    def generate_token(self):
        letters = string.ascii_letters
        print(letters)
        return ''.join(random.choice(letters) for i in range(self.token_size))