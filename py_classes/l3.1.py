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
# print(records[1])
# print(records[:1])

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


# create empty lists for branches in unique_branches
for i, num in enumerate(unique_branches):
    # print("index:" + str(i))
    # print("content:" + num)
    empty_list = []
    sales.append(empty_list)

# loop over records
for r in records:
    # consider a single record r: r[x] the name of the branch, r[y] the amount of sales
    # find the index of r[x] in unique_branches (call i(x) the index)

    # print(r[1])
    # print(r[9])
    if r[1] in unique_branches:
        branch_index = unique_branches.index(r[1])
        # append r[y] to the list of sales in position i(x)
        sales[branch_index].append(float(r[9]))

    # break

for a, b in zip(unique_branches, sales):
    c = round(sum(b), 2)
    # print(f"the sales of {a} are: {b}")
    print(f"the overall sales of {a} are: {c}")

# create a list where each item is the sum of sales of corresponding branch
overall_sales = [round(sum(x), 2) for x in sales]
# print(overall_sales)

# create a list where each item is the average of sales of corresponding branch
avg_sales = [round(sum(x) / len(x), 2) for x in sales]
# print(avg_sales)

# do the same exercise with dictionaries
sales = {}
sales_alternative = {}
for r in records:
    # is the branch in r[1] already present in sales?
    if r[1] not in sales:
        # this is a new branch
        sales[r[1]] = []
        sales[r[1]].append(float(r[9]))
        # sales[r[1]] = [float(r[9])]
    else:
        sales[r[1]].append(float(r[9]))

    # alternative solution
    if r[1] not in sales_alternative:
        sales_alternative[r[1]] = []

    sales_alternative[r[1]].append(float(r[9]))

for s in sales:
    c = round(sum(sales[s]), 2)
    print(f"the overall sales of {s} are: {c}")

sys.exit()
