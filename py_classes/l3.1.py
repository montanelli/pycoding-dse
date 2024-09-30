"""Read a csv dataset and load as a list of lists."""

import sys
import csv


# given a list in input, returns the list of uniques values
# solution with loop
def unique_values(my_list):
    # we use loops
    values = []
    for item in my_list:
        if item not in values:
            values.append(item)

    return values


# given a list in input, returns the list of uniques values
# solution with set function
def unique_values_by_set(my_list):
    my_set = set(my_list)
    return list(my_set)


# main
# open the file and read the content
with open("dataset/supermarket.csv", newline="") as f:
    reader = csv.reader(f, delimiter=",")
    records = list(reader)

# print(records)
# limit the print to the first row
print(records[1])
print(records[:1])

# skip the first row with headers
records = records[1:]

# create a list with the unique names of branches (content of the 2nd column)
branches = [row[1] for row in records]
# print(branches)
# unique_branches = unique_values(branches)
unique_branches = unique_values_by_set(branches)
print(unique_branches)

# build a list of sales by branch
# build a list of lists where each row is about a branch in unique_branches
# each row contains the list of sales of the branch in unique_branches with the same index
# consider A, B, C as branches in unique_branches
# sales will contain three items and each item is a list of sales
# the 1st item of sales is the list of sales of A, and so on...
sales = []
# try to find a solution, discussion in the next class

sys.exit()
