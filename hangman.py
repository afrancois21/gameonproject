import random
from words import science_easy_words
from words import science_medium_words
from words import science_hard_words
from words import sports_easy_words
from words import sports_medium_words
from words import sports_hard_words
from words import colors_easy_words
from words import colors_medium_words
from words import colors_hard_words
from hangmanvisual import lives_visual_dict
import string
level = input("Easy, Medium, Hard")
def difficulty_level(level):
    while level.lower() not in ["easy", "medium", "hard"]:
        print("Invalid Input")
        level = input("Easy, Medium, Hard")
    if level.lower() == "easy":
        theme = input("Science, Sports, or Colors")
        while theme.lower() not in ["science", "sports", "colors"]:
            print("Invalid Input")
            theme = input("Science, Sports, or Colors")
        if theme.lower() == "science":
            word = random.choice(science_easy_words)
            return word.upper()
        elif theme.lower() == "sports":
            word = random.choice(sports_easy_words)
            return word.upper()
        elif theme.lower() == "colors":
            word = random.choice(colors_easy_words)
            return word.upper()
    if level.lower() == "medium":
        theme = input("Science, Sports, or Colors")
        while theme.lower() != "sports" and "science" and "colors":
            print("Choose Science, Sports, or Colors")
            theme = input("Science, Sports, or Colors")
            if theme.lower() == "science":
                word = random.choice(science_medium_words)
                return word.upper()
            elif theme.lower() == "sports":
                word = random.choice(sports_medium_words)
                return word.upper()
            elif theme.lower() == "colors":
                word = random.choice(colors_medium_words)
                return word.upper()
    if level.lower() == "hard":
        theme = input("Science, Sports, or Colors")
        while theme.lower() != "sports" and "science" and "colors":
            print("Choose Science, Sports, or Colors")
            theme = input("Science, Sports, or Colors")
            if theme.lower() == "science":
                word = random.choice(science_hard_words)
                return word.upper()
            elif theme.lower() == "sports":
                word = random.choice(sports_hard_words)
                return word.upper()
            elif theme.lower() == "colors":
                word = random.choice(colors_hard_words)
                return word.upper()
def hangman():
    word = str(difficulty_level(level))
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has guessed

    lives = 7

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))

        # what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(lives_visual_dict[lives])
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else:
                lives = lives - 1  # takes away a life if wrong
                print('\nYour letter,', user_letter, 'is not in the word.')

        elif user_letter in used_letters:
            print('\nYou have already used that letter. Guess another letter.')

        else:
            print('\nThat is not a valid letter.')

    # gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print(lives_visual_dict[lives])
        print('You died, sorry. The word was', word)
    else:
        print('YAY! You guessed the word', word, '!!')

if __name__ == '__main__':
    hangman()