import random
import string
from words import words

def get_valid_word(words):
    word= random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word

def hangman():
    word= get_valid_word(words)
    word_letters= set(word)
    word_alphabet= set(string.ascii_uppercase)
    used_letters= set()

    while len(word_letters) > 0:
        print('you have already used these letters: ', ' '.join(used_letters))

        word_list= [letter if letter in used_letters else '-' for letter in word]
        print('current word: ' ,' '.join(word_list))

        user_letter = input('Guess the letter ').upper()
        if user_letter in word_alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
        elif user_letter in used_letters:
            print('You already used this letter, try again')
        else:
            print('You guessed a wrong letter')



hangman()




