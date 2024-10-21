# lamba functions
# map function

import sys
import csv


# Lambda functions are similar to user-defined functions but without a name.
# They're commonly referred to as anonymous functions. Syntax
# lambda argument(s) : expression
## lambda is a keyword in Python for defining the anonymous function.
## argument(s) is a placeholder, that is a variable that will be used to hold the value you want to pass into the function expression. A lambda function can have multiple variables depending on what you want to achieve
## expression is the code you want to execute in the lambda function.


def square_funct(n):
    return n**2


# print(square_funct(2))

square = lambda x: x**2
# print(square(3))

# lambda functions are useful when you want to apply an expression to a list of values
# this can be done in combination with the map function
# map is a Python built-in function that applies a given function to any item of a given iterable
# By default, the map() function returns a map object, which is an iterator. In many cases, we will need to convert this iterator to a list to work with the results directly.

nums_to_square = [1, 2, 3, 4, 5]
squared = list(map(square_funct, nums_to_square))

# alternative
squared = list(map(lambda x: x**2, nums_to_square))
# print(squared)

# consider the supermarket data of the last exercises
# each record contains the number of items that has been sold
# I want to calculate the normalized quantities of sold items
with open("dataset/supermarket.csv", newline="") as f:
    reader = csv.reader(f, delimiter=",")
    records = list(reader)

records.pop(0)

branches = []
items = []
# get the list of quantity items sold by each branch in each transaction
for r in records:
    # in r[1] we have the name of the current branch
    # in r[7] we have the item quantity
    if r[1] not in branches:
        # new branch
        branches.append(r[1])
        try:
            branch_quantities = [int(r[7])]
        except:
            branch_quantities = [0]
        items.append(branch_quantities)
    else:
        # the branch is already known
        branch_index = branches.index(r[1])
        try:
            items[branch_index].append(int(r[7]))
        except:
            items[branch_index].append(0)

for b, i in zip(branches, items):
    s = sum(i)
    print(f"The branch {b} has sold {s}.")

# print(items[0])
# normalize the list of quantities per branch according to Min-Max Scaling
# https://en.wikipedia.org/wiki/Feature_scaling#Rescaling_(min-max_normalization)
normalized_items = []
for i in items:
    min_value = min(i)
    max_value = max(i)

    norm_list = list(
        map(lambda x: round((x - min_value) / (max_value - min_value), 2), i)
    )
    normalized_items.append(norm_list)

print(normalized_items[0])
sys.exit()
