import random
from words import words

def get_valid_letter(words):
    word = random.choice(words)
    while "-" in word or " ":
        word = random.choice(words)

    return word.upper()

def hangman()


