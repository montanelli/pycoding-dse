import sys

# string manipulation

s = "STEfano montanelli"

# basic built-in functions
print(s.capitalize())
print(s.lower())
print(s.upper())


# string slicing (through list slicing)
# [start:stop:step]
print("result of S[0]: ", s[0])
print("result of s[1:4]: ", s[1:4])
print("result of s[-1]: ", s[-1])
print("result of s[-4:-1]: ", s[-4:-1])
print("result of s[1:]", s[1:])
print("result of s[:-1]", s[:-1])
print("result of s[-5:]", s[-5:])  # nelli
print("result of s[:-5]", s[:-5])
print("result of s[5:]", s[5:])
print("result of s[:5]", s[:5])
print("result of s[1:4:2]: ", s[1:4:2])
print("result of s[1:4]: ", s[1:4])
print("result of s[::2]: ", s[::2])  # odd elements in the string (not in index)
print("result of s[1::2]: ", s[1::2])  # even elements in the string (not in index)
print("result of s[-6:-2]: ", s[-6:-2])
print("result of s[-6:-2:-2]: ", s[-6:-2:-2])

# given a string in input, return true/false if it is a palindrome (case insensitive)
# radar, otto, civic


def check_pal(w):
    """check if a word in input is palindrome.

    Keyword arguments:
    string -- the word to evaluate

    Return:
    bool -- True when palindrome; False otherwise
    """
    w = w.lower()
    rw = w[::-1]

    # as an alternative to the if statement:
    # return w == rw
    if w == rw:
        return True
    else:
        return False


def check_pal_iteration(w):
    """check if a word in input is palindrome through iteration.

    Keyword arguments:
    string -- the word to evaluate

    Return:
    bool -- True when palindrome; False otherwise
    """
    left = 0
    right = len(w) - 1
    is_pal = True

    while left < right:
        if w[left].lower() != w[right].lower():
            is_pal = False
            # break stops the while and goes to the next operation after the loop
            break

        left += 1
        right -= 1

    return is_pal


# main code
word = "abcd45dcba"

if check_pal_iteration(word):
    # have a look at the print function in Python:
    # https://docs.python.org/3/tutorial/inputoutput.html
    print(f"the '{word}' is palindrome")
else:
    print(f"the '{word}' is not palindrome")

sys.exit()

# more exercises on string manipulations:
# https://www.geeksforgeeks.org/python-string-exercise/
# use a serch engine for more
