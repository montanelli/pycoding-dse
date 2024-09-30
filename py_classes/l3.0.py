import sys

# use of lists
items = [1, 2, 3, 4, 5, 6]
# alternative syntax
items = list((1, 2, 3, 4, 5, 6))
print(items)

# example with strings
items = ["summer", "autumn", "winter"]
print(len(items))
print(items[0])

items.append("spring")
print(len(items))

# iterate over the list
for i in items:
    print(i)

# what is the output of this command?
print(list(range(len(items))))

# list sorting
print(items)
items.sort()
print(items)

# discover how sorting is performed in Python
# have a look at the quicksort, mergesort
# exercise: try to implement quicksort as a custum function

# list slicing
# list of dwarfs
dwarfs = ["Doc", "Bashful", " Grumpy", "Sneezy", "Happy", "Sleepy", "Dopey"]
print(dwarfs)
print(dwarfs[1:5])
print(dwarfs[:5])
print(dwarfs[5:])
print(dwarfs[:5] + dwarfs[5:])
print(dwarfs[:])
print(dwarfs[1:5])
print(dwarfs[1:5:2])
print(dwarfs[-1])
print(dwarfs[-5:-1])
print(dwarfs[-1:-5:-1])
print(dwarfs[::-1])

# exercise: given a list, reverse the left with the right part
# (calculate the middle index, and then use slicing to reverse)

# list of lists
A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(A)
print(A[1])
print(A[1][2])
print(A[0][-1])
# get the items of the last column
last_column = []
for item in A:
    # get the last item of the row
    last_column.append(item[-1])

# same with list comprehension
last_column = [row[-1] for row in A]
print(last_column)

sys.exit()
