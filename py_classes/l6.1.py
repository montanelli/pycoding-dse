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

print("Welcome to WORDLE!")
print(f"Guess the target word, you have {max_attempts} tries.")

# work on your solution, discussion in the next classes

sys.exit()
