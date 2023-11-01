import random
from words import words
import string

def get_valid_letter(words):
    word = random.choice(words)
    while "-" in word or " ":
        word = random.choice(words)

    return word.upper()

def hangman():
    alphabet = set(string.ascii_uppercase)
    word = get_valid_letter(words)
    word_letters = set(word)
    used_letters = set()

    user_letter = ("Guess a letter").upper()
    if user_letter in alphabet - used_letters:
        print("Correct")
        used_letters.add(user_letter)
    if user_letter in word_letters:
        word_letters.remove(user_letter)
    elif user_letter in used_letters:
        print("You have already used this letter")












