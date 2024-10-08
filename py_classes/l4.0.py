import string
import re
from collections import Counter

# focus on dictionaries
capitals = {"Italy": "Rome", "France": "Paris", "Germany": "Berlin"}

# print(capitals)
# print(capitals.keys())
# print(capitals.values())
# print(capitals["Italy"])

capitals["Spain"] = "Madrid"
# print(capitals)

# this raises a KeyError: missing key
# print(capitals["Austria"])

# use get() to avoid keyError when key is missing
# print(capitals.get("Austria"))

# exercise: count the occurrences of each word in a text
# read the content of the text from file
my_file = open("dataset/Bohemian_rhapsody_lyrics.txt", "r", encoding="UTF-8")
my_text = my_file.read()
# print(my_text)

# drop punctuation
# method 1. list comprehension
print(string.punctuation)
cleaned_text = [x for x in my_text if x not in string.punctuation]
cleaned_text = "".join(cleaned_text)


# method 2. regular expressions
# \s any whitespace, newline, newtab
# \w any alphanumerical char including letters and numbers
cleaned_text = re.sub(r"[^\s\w]", "", my_text)

# method 3. transform the text through translation table
translation_table = str.maketrans("", "", string.punctuation)
cleaned_text = my_text.translate(translation_table)
# print(cleaned_text)

# reduce the capitalization of letters
my_lower_text = cleaned_text.lower()

# split words
my_split_text = my_lower_text.split()
print(my_split_text)

# count occurrences
word_count = {}
for word in my_split_text:
    if word not in word_count:
        # new word (never met before): add item to dict
        word_count[word] = 1
    else:
        # word already met, already stored in word_count, so increase the counter
        word_count[word] += 1

# print(word_count)
# pretty printing the dict
for w in word_count:
    print(f'The word "{w}" has frequency {word_count[w]} in the text.')

# exercise: show the dict from top frequent to least frequent
# try to find a solution


# find the top frequent item in the dict
# method 1. Use Counter
print(type(word_count))
word_count_counter = Counter(word_count)
print(type(word_count_counter))

# print the top occuring item in word_count
print(word_count_counter.most_common(1))
