"""Play Wordle with Python. Object-oriented version."""

import sys
import csv
from random import choice
from termcolor import colored
from datetime import datetime


def load_dict():
    with open("dataset/en_unigram_freq.csv", newline="") as f:
        reader = csv.reader(f, delimiter=",")
        records = list(reader)

    # skip the first row with headers
    records = records[1:]

    # drop frequencies
    words = [r[0] for r in records]

    # keep only words with len 5 (switch to uppercase)
    word5 = [i.upper() for i in words if len(i) == 5]

    return word5


class Wordle:

    max_attempts = 6

    target_word = None

    en_5_dict = []
    guess_history = []
    colored_history = []
    tile_history = []

    def __init__(self, attempts=None):
        if attempts is not None:
            self.max_attempts = attempts

        # load the dictionary
        self.en_5_dict = load_dict()

        # pick the target
        self.set_target()
        self.print_target()

    # set the target
    def set_target(self):
        self.target_word = choice(self.en_5_dict)

    # print the target
    def print_target(self, f=None):
        if f is not None:
            f.write(f"The target word is {self.target_word}.\n")

        print(f"The target word is {self.target_word}.")

    def print_history(self, f=None):
        for i, g in enumerate(self.guess_history):
            if f is not None:
                f.write(f"Attempt {i+1}: {g}.\n")

            print(f"Attempt {i+1}: {g}.")

    def print_feedback_last(self):
        print(self.colored_history[-1], end=" ")
        print(self.tile_history[-1])

    def print_feedback_all(self):
        for c, t in zip(self.colored_history, self.tile_history):
            print(c, end=" ")
            print(t)

    # add a guess to history
    def add_to_history(self, guess):
        self.guess_history.append(guess)

    # add a guess to colored history
    def add_to_colored(self, guess):
        self.colored_history.append(guess)

    # add a guess to tile history
    def add_to_tile(self, guess):
        self.tile_history.append(guess)

    def save_game(self):
        # file modalities: w (write and overwrite) - a (append) - r (read)
        f = open("wordle.txt", "a")
        now = datetime.now()
        now_string = now.strftime("%d/%m/%Y %H:%M:%S")
        f.write(f"Wordle is played on {now_string}.\n")
        self.print_target(f)
        self.print_history(f)
        f.close()

    def __del__(self):
        self.save_game()

    # new version of validate_guess where we first process the letters in the correct place, than the others
    def validate_guess(self, guess):
        tiles = {"correct_place": "🟩", "correct_letter": "🟨", "incorrect": "⬛"}
        guessed = []
        pattern = []

        correct_places = list(map(lambda x, y: x == y, guess, self.target_word))
        # [f(x) if condition else g(x) for x in sequence]
        target = "".join(
            [y if not x else "-" for x, y in zip(correct_places, self.target_word)]
        )
        # print(correct_places)
        # print(target)

        correct_letters = list(map(lambda x: x in target, guess))
        # print(correct_letters)

        for i, (x, y) in enumerate(zip(correct_places, correct_letters)):
            if x:
                guessed.append(colored(guess[i], "green"))
                pattern.append(tiles["correct_place"])
            elif y:
                guessed.append(colored(guess[i], "yellow"))
                pattern.append(tiles["correct_letter"])
            else:
                guessed.append(guess[i])
                pattern.append(tiles["incorrect"])

            # print(target)

        # add the joined colored letters and tiles pattern to history
        self.add_to_colored("".join(guessed))
        self.add_to_tile("".join(pattern))

    def play_game(self):
        print("Welcome to WORDLE!")
        print(f"Guess the target word, you have {self.max_attempts} tries.")

        is_guessed = False
        attempt = 1

        # Keep playing until the user runs out of tries or finds the word
        while (not is_guessed) and (attempt <= self.max_attempts):

            bad_guess = True
            # Check the correctness of the user guess
            while bad_guess:
                guess = input(
                    f"Attempt number {attempt}. Insert a 5-letter word:"
                ).upper()
                # If the guess was already used
                if guess in self.guess_history:
                    print("You have already guessed this word!")
                # If the guess has not 5 letters
                elif len(guess) != 5:
                    print("Please enter a 5-letter word!")
                # If the guess is not in the dictionary
                elif guess not in self.en_5_dict:
                    print("This word does not exist!")
                else:
                    bad_guess = False

            # Append the guess to history
            self.add_to_history(guess)

            # Validate the guess
            self.validate_guess(guess)

            # self.print_feedback_last()
            self.print_feedback_all()

            if guess == self.target_word:
                is_guessed = True
            else:
                attempt += 1

        # print a final message
        if not is_guessed:
            print(f"Sorry, you missed the target: {self.target_word}")
        else:
            print(f"Well done, congratulations! You did it in {attempt} tries.")


# the use of this method avoids error on the use of open in object destroyer
# https://stackoverflow.com/questions/26544076/how-to-achieve-file-write-open-on-del
def wordle_creation(attempts):
    wordle = Wordle(attempts)
    wordle.play_game()


# main
wordle_creation(5)

sys.exit()
