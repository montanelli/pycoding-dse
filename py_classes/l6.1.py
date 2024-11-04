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
from datetime import datetime

# setup
max_attempts = 6
save_on_file = True
tiles = {"correct_place": "🟩", "correct_letter": "🟨", "incorrect": "⬛"}


# check_guess returns colored letters and colored tiles that are the feedback on a letter-by-letter comparison of guess against target
# this solution is not completely satisfactory. There are cases where the letters are not properly colored (can you find a solution?). Example:
# guess: canal
# target: medal
def check_guess_old(guess, target):
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


def check_guess(guess, target):
    # global means that a variable defined in the main code is visible and accessible in the function scope
    global tiles

    colored_letters = []
    colored_tiles = []

    # manage the green case (correct letters in proper position)
    correct_letters = list(map(lambda x, y: x == y, guess, target))
    # replace the correct letters with hyphen
    target = "".join([y if not x else "-" for x, y in zip(correct_letters, target)])

    # manage the yellow case (right letters in wrong position)
    yellow_letters = list(map(lambda x: x in target, guess))

    for i, (x, y) in enumerate(zip(correct_letters, yellow_letters)):
        if x:
            # color in green
            colored_letters.append(colored(guess[i], "green"))
            colored_tiles.append(tiles["correct_place"])
        elif y:
            # color in yellow
            colored_letters.append(colored(guess[i], "yellow"))
            colored_tiles.append(tiles["correct_letter"])
        else:
            # color in grey
            colored_letters.append(guess[i])
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
# target = "MEDAL"
# print the target for debugging
print("the target is: " + target)

print("Welcome to WORDLE!")
print(f"Guess the target word, you have {max_attempts} tries.")
print("Print 'quit' to finish the game.")

# list of previous attempts and colored guesses
history = []
colored_letters = []
colored_tiles = []
# current attempt
attempt = 1
is_guessed = False
is_stopped = False
# while loop: consider the number of attempts (that needs to be lower than the maximum)
while (attempt <= max_attempts) and (not is_guessed) and (not is_stopped):

    # loop over the input until a "rule-compliant" guess is inserted by the user
    is_input_ok = False
    while not is_input_ok:
        # enter the guess
        guess = input(f"Attempt number {attempt}. Insert a 5-letter word: ")
        guess = guess.upper()

        if guess.lower() == "quit":
            is_stopped = True
            break

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
            is_input_ok = True

    if not is_stopped:
        # check the correctness of letters
        c_letters, c_tiles = check_guess(guess, target)

        # print a feedback
        print(c_letters)
        print(c_tiles)

        # update history
        history.append(guess)
        colored_letters.append(c_letters)
        colored_tiles.append(c_tiles)

        if guess == target:
            is_guessed = True
        else:
            # increase the counter
            attempt += 1


# provide a feedback when the target is missed
if is_guessed:
    print(f"Good job! the target is guessed in {attempt} times!")
elif is_stopped:
    print("Thank you for playing. Bye bye.")
else:
    print(f"You missed the target word: {target}. Play again.")


# save the tries on a file
if save_on_file:
    # file modalities: w (write and overwrite) - a (append) - r (read)
    f = open("wordle.txt", "a")
    now = datetime.now()
    now_string = now.strftime("%d/%m/%Y %H:%M:%S")
    f.write(f"Wordle is played on {now_string}.\n")
    f.write(f"The target word is {target}.\n")
    for i, g in enumerate(history):
        f.write(f"Attempt {i+1}: {g}.\n")
    f.write("\n")
    f.close()


sys.exit()
