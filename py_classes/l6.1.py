# we want to implement the Wordle game
# https://www.nytimes.com/games/wordle/index.html

# you have X attempts to guess the target word that is randomly selected within the 5-letter words in English

# rules:
## A correct letter turns green
## A correct letter in the wrong place turns yellow
## An incorrect letter turns gray

# for any attempt, the feedback must report green-yellow-gray letters
# use tiles to provide a feedback (see the pic in the attachment)


# cases to handle (with a message to the player)
# words that are not in the dictionary
# words with length different from 5
# words already guessed (do not consume tries, we need a history)

import sys
import csv
from random import choice
from termcolor import colored

# setup
max_attempts = 6
tiles = {"correct_place": "🟩", "correct_letter": "🟨", "incorrect": "⬛"}


# check_guess returns colored letters and colored tiles that are the feedback on a letter-by-letter comparison of guess against target
# this solution is not completely satisfactory. There are cases where the letters are not properly colored (can you find a solution?). Example:
# guess: canal
# target: medal
def check_guess(guess, target):
    # global means that a variable defined in the main code is visible and accessible in the function scope
    global tiles

    colored_letters = []
    colored_tiles = []

    for i, letter in enumerate(guess):
        if guess[i] == target[i]:
            # color in green
            colored_letters.append(colored(letter, "green"))
            colored_tiles.append(tiles["correct_place"])
        elif guess[i] in target:
            # color in yellow
            colored_letters.append(colored(letter, "yellow"))
            colored_tiles.append(tiles["correct_letter"])
        else:
            # color in grey
            colored_letters.append(letter)
            colored_tiles.append(tiles["incorrect"])

        # print(colored_tiles)
        # print("".join(colored_tiles))

    return "".join(colored_letters), "".join(colored_tiles)


# main
# load the EN dictionary and isolate the 5-letter words
with open("dataset/en_unigram_freq.csv", newline="") as f:
    reader = csv.reader(f, delimiter=",")
    records = list(reader)

records.pop(0)
# print(records[0])

# drop the frequencies
# [f(x) for x in iterable]
en_words = [x[0] for x in records]
# print(en_words)

# limit to 5 letter-words and switch to uppercase
# [f(x) for x in iterable if condition]
en_words_5 = [x.upper() for x in en_words if len(x) == 5]
# print(en_words_5[100:106])
# print(len(en_words_5))

# pick-up the target
# more sophisticated methods for choosing the target are possible
# consider random.choices that allows to consider weights associated with words
# the word frequencies could be used to make more probable the words that are less frequent
# this way, it is possible to define the game difficulty
target = choice(en_words_5)
target = "MEDAL"
print("the target is:" + target)

print("Welcome to WORDLE!")
print(f"Guess the target word, you have {max_attempts} tries.")


# list of previous attempts and colored guesses
history = []
colored_letters = []
colored_tiles = []
# current attempt
attempt = 1

# while loop: consider the number of attempts (that needs to be lower than the maximum)
while attempt <= max_attempts:
    # enter the guess
    guess = input(f"Attempt number {attempt}. Insert a 5-letter word:")

    guess = guess.upper()

    if guess == target:
        print("Good job! the target is guessed!")
        # move attempts over the max, so the loop is stopped
        attempt = max_attempts + 1

    # check possible errors in the attempt:
    # not in EN dict, not 5 letters, already in the history
    if len(guess) != 5:
        print("Please, insert a 5-letter word!")
    elif not guess.isalpha():
        print("Please, insert a 5-letter word!")
    elif guess in history:
        print("This guess is already tried, try another one!")
    elif guess not in en_words_5:
        print("Please, insert a word in the English dictionary")
    else:
        # if the guess is the target or provide a feedback
        history.append(guess)
        c_letters, c_tiles = check_guess(guess, target)

        print(c_letters)
        print(c_tiles)

        colored_letters.append(c_letters)
        colored_tiles.append(c_tiles)

        # increase the counter
        attempt += 1

# provide a feedback when the target is missed

sys.exit()
